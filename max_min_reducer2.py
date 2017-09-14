#! /usr/bin/env python

import sys

max = 0 
last_key = False

for line in sys.stdin:
  data = line.split('\t')
  key = data[0].split('_')
  year = key[0]
  word = key[1]
  sum = int(data[1])

  # if new key, emit current count
  if(last_key and word != last_key):
    if(sum > max):
      max = sum
  last_key = word

  else:
    print(word+'\t'+max)
