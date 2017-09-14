#! /usr/bin/env python
import sys

# reducer aggregate word
count = 0
sum = 0
last_key = False

# expecting <year_word, count>
for line in sys.stdin:
  data = line.split("\t")
  year = data[0]
  word = data[1]
  org_count = data[2]
  current_key = year + '_' + word

  # found new key, emit current count
  if last_key and current_key != last_key:
    print(current_key+'\t'+total)
    last_key = current_key
    count += 1
    sum = org_count

  # increment count
  else:
    last_key = current_key
    count += 1
    sum += org_count

# last key
if last_key:
  print(last_key+'\t'+total)
