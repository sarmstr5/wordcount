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
partition = 1985
year = 1985

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
            date = year

    words = doc.split()
    for word in words:
        word_dict[word] += 1

    for word in sorted(word_dict.iterkeys()):
        print('{}\t{}\t{}\t{}'.format(partition, date, word, word_dict[word]))

    if(term_year == term_window):
        partition += 4
        term_year = 0
    else:
        term_year += 1

    year += 1




