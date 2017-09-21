#! /usr/bin/env python

import sys
from collections import defaultdict
import ast
import numpy as np

# initializes values as zeros array of length i when new key is added
# made it 6 incase of multiple sotu addresses in one year
# word_dict = defaultdict(lambda : [0]*6)
word_dict = defaultdict(int)

# looking at partitioning the addresses into 'presidential terms'
# years start at zero due to list indexing
# the term window is one year longer to store the camparison year
term_window = 4
term_year = 0
year_partition = 1985
year = 1985

# because partition is an int starting at 0 i could do a list of tuples for
# all_counts
all_counts = defaultdict(list)
doc_counts = defaultdict(lambda : [0]*5)
sig_words = defaultdict(list)
cur_partition = None
first_year = 1989

def calc_avg_std(word_counts):
  previous_counts = word_counts[:-1]
  x = word_counts[-1]
  avg = np.mean(previous_counts)
  std = np.std(previous_counts)
# if x == 0 or avg == 0:
#   return 0
  z_score = (x - avg)/(std)
  return abs(round(z_score,2))


# input from STDIN
# expecting a year, word, list of 5 word counts from each year 
# 1985 \t young \t 6
for line in sys.stdin:
  term_partition, word, counts = line.split('\t')
  try:
      counts = ast.literal_eval(counts)
      # do i need to error test this?
      counts = [int(i) for i in counts]
      term_partition = int(term_partition)
  except ValueError:
      continue

    # want the words to be sorted by partition for the reducer
    # sorted words for validation purposes but not needed
    # should this if be first?
    if term_year == term_window:
        print('in new term year {}'.format(year))
        for word in sorted(word_dict.iterkeys()):
#           print('{}\t{}\t{}'.format(year_partition, word, word_dict[word]))
            if word_dict[word][term_window] == 0:
              del word_dict[word]
            else:
              # shift count from index 4 to 0
              word_dict[word] = [word_dict[word][term_window], 0, 0, 0, 0]
        term_year = 0
        year_partition += 4
        year+=1
        
    else:
        print('same term year {}'.format(year))


  new_term = first_year + 4 * term_partition
  print(new_term)
  # if new document, the previous document is completed
  # calc average
  # create new doc dictionary to restart word count
  if cur_partition and (cur_partition != term_partition):
    for word, counts in doc_counts.iteritems():
      z_score = calc_avg_std(counts)
      if z_score > 2:
        all_counts[new_term].append((word, z_score))
        print('{}\t{}\t{}'.format(new_term, word, z_score))
    doc_counts = defaultdict(int)

  # same partition
  else:
    cur_partition = term_partition
    for i in range(len(counts)):
      doc_counts[word][i] += counts[i]

# went through all mapped items
for term, term_list in all_counts.iteritems():
  for tup in term_list:
    (word, z_score) = tup
    print('{}\t{}\t{}'.format(term, word, z_score))
