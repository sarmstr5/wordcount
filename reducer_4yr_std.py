#! /usr/bin/env python

import sys
from collections import defaultdict
import ast
import numpy as np


# because partition is an int starting at 0 i could do a list of tuples for
# all_counts
all_counts = defaultdict(list)
doc_counts = defaultdict(lambda : [0]*6)
sig_words = defaultdict(list)
cur_partition = None
first_year = 1989

def calc_avg_std(word_counts):
  previous_counts = word_counts[:-1]
  x = word_counts[-1]
  avg = np.mean(previous_counts)
  std = np.std(previous_counts)
  z_score = (x - avg)/(std)
  return abs(round(z_score,2))


# input from STDIN
# expecting partition \ year \ word \ year
# 0 \t 1985 \t young \t 6
for line in sys.stdin:
  cur_partition, year, word, count = line.split('\t')
  try:
      count = int(count)
      term_partition = int(term_partition)
  except ValueError:
      continue
    # want the words to be sorted by partition for the reducer
    # sorted words for validation purposes but not needed
    # should this if be first?


  new_term = first_year + 4 * term_partition
  print(new_term)
  # if new document, the previous document is completed
  # calc average
  # create new doc dictionary to restart word count
  if cur_partition and (cur_partition != last_partition):
    for word, counts in doc_counts.iteritems():
      z_score = calc_avg_std(counts)
      if z_score > 2:
        all_counts[new_term].append((word, z_score))
        print('{}\t{}\t{}'.format(new_term, word, z_score))
    doc_counts = defaultdict(int)

  # same partition
  else:
    for i in range(len(counts)):
      doc_counts[word][i] += counts[i]
  cur_partition = term_partition

