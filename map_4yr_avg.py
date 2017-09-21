#! /usr/bin/env python

import os
import sys
import re
from collections import defaultdict

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



