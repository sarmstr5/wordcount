#! /usr/bin/env python

import sys
from collections import defaultdict
import ast
import numpy as np

all_counts = defaultdict(list)
doc_counts = defaultdict(int)
sig_words = defaultdict(list)
cur_partition = None
first_year = 1989

def calc_avg_std(word_counts):
  previous_counts = word_counts[:-1]
  x = word_counts[-1]
  avg = np.mean(previous_counts)
  std = np.std(previous_counts)
  sqrt_n = len(previous_counts)**(0.5)
  if x == 0 or avg == 0:
    return 0
  t_score = (x - avg)/(std/sqrt_n)
  return abs(round(t_score,2))


# input from STDIN
# expecting a partition number, word, list of 5 word counts from each year 
# 1 \t young \t [3,1,3,5,6]
for line in sys.stdin:

    term_partition, word, counts = line.split('\t')
    try:
        counts = ast.literal_eval(counts)
        # do i need to error test this?
        counts = [int(i) for i in counts]
        term_partition = int(term_partition)
    except ValueError:
        continue

    new_term = first_year + 4 * term_partition
    # if new document, the previous document is completed
    # calc average
    # create new doc dictionary to restart word count
#   if cur_partition and (cur_partition != term_partition):
#       for year, word in doc_counts.iteritems():
#         print('{}\t{}'.format(year, word))
#       doc_counts = defaultdict(int)

    # same partition
#   else:
    t_score = calc_avg_std(counts)
    if t_score > 2:
#       all_counts[new_term].append((word, t_score))
#     print(counts)
      print('{}\t{}\t{}'.format(new_term, word, t_score))
    cur_partition = term_partition

# went through all mapped items
