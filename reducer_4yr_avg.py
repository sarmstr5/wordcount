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
last_partition = None
first_year = 1989

def calc_avg_std(word_counts):
  avg = np.mean(word_counts)
  return abs(round(avg, 2))


# input from STDIN
# expecting partition_year \ year \ word \ year
# 1985 \t 1986 \t young \t 6
for line in sys.stdin:
    cur_partition, year, word, count = line.split('\t')
    try:
      count = float(count)
      cur_partition = int(cur_partition)
      year = int(year)
    except ValueError:
      continue

    
    dict_index = year - cur_partition
    # if new document, the previous document is completed
    # calc average
    # create new doc dictionary to restart word count
    if cur_partition and (cur_partition != last_partition):
        for word, counts in doc_counts.iteritems():
            avg = calc_avg_std(counts)
            print('{}\t{}\t{}'.format(year, word, avg))
            doc_counts = defaultdict(lambda : [0]*6)

  # same partition
    else:
        doc_counts[word][dict_index] += count
    last_partition = cur_partition
    

