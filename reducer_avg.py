#! /usr/bin/env python

import sys

current_word = None
current_count = 0
word = None
word_counts = {}
sum = 0.0

#input from STDIN
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    # works because hadoop sorts map output
    # same word
    if current_word == word:
       current_count += count
       sum += count

    # new word, save word count and start new
    else:
        if current_word:
            word_counts[current_word] = current_count
        current_count = count
        current_word = word
        sum += count

# went through all mapped items
for word, count in word_counts.iteritems():
    print('{}\tcount: {}\tavg use per word: {}'.format(word, count, 
                                                       round(float(count/sum), 4)))
    
