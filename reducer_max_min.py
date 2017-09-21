#! /usr/bin/env python

import sys
from collections import defaultdict

all_counts = defaultdict(list)
doc_counts = defaultdict(int)
current_doc = None
last_doc = None

# input from STDIN
# expecting a doc number, word from document, and count for that word
for line in sys.stdin:
    current_doc, word, count = line.split('\t')
    print( 'new doc: {} word:{} count:{}'.format(current_doc, word, count)) 
    try:
        count = int(count)
    except ValueError:
        continue

    # expecting hadoop to give keys sorted by doc with words in arbituary order
    # if new document the previous document is completed
    # append word counts for that document to master word count dictionary 
    # create new doc dictionary to restart word count
    if current_doc and (current_doc != last_doc):
        print('in new doc')
        for word, count in doc_counts.iteritems():
            all_counts[word].append(count)
        doc_counts = defaultdict(int)


    # same document continue incrementing document word counts
    else:
        print('same doc')
        last_doc = current_doc
        doc_counts[word] += count

# went through all mapped items
print('went though mapped items')
for word, counts in all_counts.iteritems():
    print(word)
    print(counts)
    max_wc = max(counts)
    min_wc = min(counts)
    print('{}\t{}\t{}'.format(word, min_wc, max_wc))
