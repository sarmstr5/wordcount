cat 2017022.txt | python average_by_attribute_mapper.py | sort -k1,1 | python test_reducer.py
for f in *.txt; do (cat "${f}"; echo) done
awk 'FNR==1 && NR>1{print ""}1' *.txt

for f in *.txt; do (cat "${f}"; echo) done | python2 map_4yr_avg.py | sort -k1,1 | python2 reducer_4yr_avg.py
