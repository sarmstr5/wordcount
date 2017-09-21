#! /uxr/bin/env python

import sys
import os

input_file = os.environ['map_input_file']
year =  int(sys.argv[1])
for line in sys.stdin:
  words = line.strip().split()
  for word in words:
    print(year+'\t'+word+'\t'+str(1))

