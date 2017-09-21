#! /usr/bin/env python

import os
import sys
import re
from collections import defaultdict

# initializes values as zeros array of length i when new key is added
# made it 6 incase of multiple sotu addresses in one year
# word_dict = defaultdict(lambda : [0]*6)
word_dict = defaultdict(int)

# looking at partitioning the addresses into 'presidential terms'
# years start at zero due to list indexing
# the term window is one year longer to store the camparison year
term_window = 3
term_year = 0
year_partition = 1985
year = 1985
doc_count = 0

for doc in sys.stdin:
    try:
        # files are YYYYMMDD.txt
        input_file = os.environ['mapreduce_map_input_file']
        date = input_file.split('.')[0][:4]
    except KeyError:
        try:
            input_file = os.environ['map_input_file']
            date = input_file.split('.')[0][:4]
        except KeyError:
            date = doc_count

    words = doc.split()
    for word in words:
      word_dict[word] += 1
    for word, count in sorted(word_dict.iterkeys()):
      print('{}\t{}\t{}'.form(date, word, count)
    doc_count += 1

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
    term_year += 1
    year += 1


