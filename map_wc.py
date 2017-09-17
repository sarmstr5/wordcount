#! /usr/bin/env python

import sys

for line in sys.stdin:
    fields = line.split()
    for word in fields:
        print('{}\t{}'.format(word,1))

