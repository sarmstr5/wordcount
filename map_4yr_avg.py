#! /usr/bin/env python

import os
import sys
import re
from collections import defaultdict

# initializes values as zeros array of length 5 when new key is added
word_dict = defaultdict(lambda : [0]*5)

# looking at partitioning the addresses into 'presidential terms'
# years start at zero due to list indexing
# the term window is one year longer to store the camparison year
term_window = 4
term_year = 0
year_partition = 0

for doc in sys.stdin:
    data = doc.split()
    for line in data:
        words = line.split()
        for word in words:
              word_dict[word][term_year] += 1

    # want the words to be sorted by partition for the reducer
    # sorted words for validation purposes but not needed
    if term_year == term_window:
        print('in if loop')
        for word in sorted(word_dict.iterkeys()):
            print('{}\t{}\t{}'.format(year_partition, word, word_dict[word]))
            if word_dict[word][term_window] == 0:
              del word_dict[word]
            else:
              word_dict[word] = [word_dict[word][term_window], 0, 0, 0, 0]
        term_year = 0
        year_partition += 1
    else:
        print('year count ++')
        term_year += 1


