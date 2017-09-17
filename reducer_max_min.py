#! /usr/bin/env python

import sys
from collections import defaultdict

all_counts = defaultdict(list)
doc_counts = defaultdict(int)
current_doc = None

# input from STDIN
# expecting a doc number, word from document, and count for that word
for line in sys.stdin:

    doc_num, word, count = line.split('\t')

    try:
        count = int(count)
    except ValueError:
        continue

    # expecting hadoop to give keys sorted by doc with words in arbituary order
    # if new document the previous document is completed
    # append word counts for that document to master word count dictionary 
    # create new doc dictionary to restart word count
    if current_doc and (current_doc != doc_num):
        for word, count in doc_counts.iteritems():
            all_counts[word].append(count)
        doc_counts = defaultdict(int)


    # same document continue incrementing document word counts
    else:
        current_doc = doc_num
        doc_counts[word] += count

# went through all mapped items
try:
    for word, counts in all_counts.iteritems():
        max_wc = max(counts)
        min_wc = min(counts)
        print('{}\t{}\t{}'.format(word, min_wc, max_wc))
except:
    print(Exception)
