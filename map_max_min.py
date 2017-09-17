#! /usr/bin/env python

import os
import sys
import re
from collections import defaultdict

# initializes value as zero when new key is added
word_dict = defaultdict(int)
doc_count = 0

#input_file = os.environ['map_input_file']
#date = input_file.split('.')[0]
#date = int(re.search('\d+', input_file)
#for a in os.environ:
#    print('Var: {}\tValue: {}'.format(a, os.getenv(a)))

for doc in sys.stdin:
    data = doc.split()
    print(data)
    for line in data:
        words = line.split()
        for word in words:
            # to save network traffic
            word_dict[word] += 1

    for word in sorted(word_dict.iterkeys()):
        # want the words to be sorted by year for the reducer
        print('{}\t{}\t{}'.format(doc_count, word, word_dict[word]))

#    for word, count in sorted(word_dict.items():
        # want the words to be sorted by year for the reducer
#        print('{}\t{}\t{}'.format(doc_count, word, count))
    word_dict = defaultdict(int)
        
    doc_count += 1

