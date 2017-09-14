#! /usr/bin/env python

import sys

(last_key, sum, count) = (None, 0, 0)
total=0
last_key = False

for line in sys.stdin:
  data = line.split("\t")
  year = data[0]
  word = data[1]
  count = data[2]
  combined_key = year + '_' + word
  
  # found new key, emit current count
  if last_key and current_key != last_key:
    print(current_key, total)
    last_key = current_key
    total = count


  # same key increment count
  else:
    last_key = current_key
    total += count

# last key
if last_key:
  print(last_key, total)

