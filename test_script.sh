cat 2017022.txt | python average_by_attribute_mapper.py | sort -k1,1 | python test_reducer.py
for f in *.txt; do (cat "${f}"; echo) done
awk 'FNR==1 && NR>1{print ""}1' *.txt

for f in *.txt; do (cat "${f}"; echo) done | python2 map_4yr_avg.py | sort -k1,1 | python2 reducer_4yr_avg.py

hadoop jar  /apps/hadoop-2.4.1/share/hadoop/tools/lib/hadoop-streaming-2.4.1.jar -input input/2017022.txt -output max_min_output2 -file ~/src/map_max_min.py -mapper ~/src/map_max_min.py -file  ~/src/reducer_max_min.py -reducer ~/src/reducer_max_min.py
