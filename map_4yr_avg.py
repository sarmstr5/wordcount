#! /usr/bin/env python

import os
import sys
import re
from collections import defaultdict

# initializes value as zero when new key is added
word_dict = defaultdict(int)

# looking at partitioning the addresses into 'presidential terms'
term_window = 4
year_count = 1
year_partition = 0

#input_file = os.environ['map_input_file']
#date = input_file.split('.')[0]
#date = int(re.search('\d+', input_file)
#for a in os.environ:
#    print('Var: {}\tValue: {}'.format(a, os.getenv(a)))

for doc in sys.stdin:
    data = doc.split()
    for line in data:
        words = line.split()
        for word in words:
            # to save network traffic save in dictionary and print summed counts
            word_dict[word] += 1


    # want the words to be sorted by partition for the reducer
    # sorted words for validation purposes but not needed
    if year_count == term_window:
        for word in sorted(word_dict.iterkeys()):
            print('{}\t{}\t{}'.format(year_partition, word, word_dict[word]))
        year_count = 1
        year_partition += 1
        word_dict = defaultdict(int)  # overwrite dictionary to save RAM
    else:
        year_count += 1

