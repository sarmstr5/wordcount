#! /usr/bin/env python

import os
import sys
from collections import defaultdict

# initializes value as zero when new key is added

word_dict = defaultdict(int)
doc_count = 0

for doc in sys.stdin:
    try:
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
        # to save network traffic
        word_dict[word] += 1

    # dont need to sort words but helps with validation
    for word in sorted(word_dict.iterkeys()):
        print('{}\t{}\t{}'.format(date, word, word_dict[word]))

    word_dict = defaultdict(int)
    doc_count += 1

