4) compute max and min a word appears in all addresses
let wordcount_map(file, firstyear, lastyear)
  for each address in addresses
    year = get_year_from_address(address)
    for each line in address
      for each word in line
        emit(<year, [word, 1]>)
// how do i loop through map phase?  I dont think i can this has to handled some other way i think

// does having this many partitions/reducers cause problems?problems
let max_min_wc_partitioner(<year, word>, first_year, last_year)
  partition = 0
  partition_hashmap = new hashmap
  for year from first_year to last_year:
    partition_hashmap[year] = partition
    partition ++

  
let max_min_wc_reduce(wordcount_map)
  if 
  for each key
    key_hashmap[word]++
  for each key in key_hashmap
      if master_hashmap[key] < key_hashmap[key]
        master_hashmap[key] == key_hashmap[key]

5) Compute avg and std of words in 4 year windows from 1985

start_year = 1985
year = start_year
while year < 2018
  term_year = 0
// does it make more sense to make multiple files or store inline on 1 file 
  term_avg_wcs = empty list
  term_std_wcs = empty list 

  // pull file locations from local directory then merge to hdfs
  while term_year < 3
    address = get_file_location(year)
    append address to addresses
    term_year++
  year += 4

  // merge local address files into one hdfs file to reduce network costs
  hdfs_addresses = merge_dfs(addresses)

  //map
  // not sure if we need to do each address, can skip that loop
  let map(file):
    for each address in hdfs_addresses
      for each line in address
        for each word in line
          emit(<word, 1>)

  // I am assuming that the years start on the term shift
  // partition 
  let partitioner(<year, word>, first_year, last_year)
    i = 0
    partition = 0
    partition_hashmap = new hashmap
    for year from first_year to last_year:
      if i == 3
        i = 0
        partition ++
      partition_hashmap[year] = partition

  //reduce
  let reduce(mapped_keys):
    for each k_v_pairs in mapped_keys
      sum = 0
      count = 0
      key , values = split(k_v_pair)
      for each value in values
        sum += value
        count++
      emit(key, sum, count)
  let write_file(reduced_output):
    filename = year
    open file as filename
    for each key
      write(key, sum, count) // "key:sum,count\t" thinking about need for sort but if i read as dictionary no need to sort
    close file

6) In post window years, find words whose use was greater than 2 stds (e.g. 89)
6.a) post window years
year = start_year + 4
while year < 2018
  wordcount_map(stdin)
  wordcount_reduce(map_output)
  write_file(reduced_output)
  year += 4

6.b) find statstically significant words
year = start_year + 4

while year < 2018
  statistically_significant_words = new list
  significant_words_by_year = new hashmap
  previous_presidency_sotu = read_in_addresses(year-4, year-3, year-2, year-1)
  new_presidency_sotu = read_in_addresses(year)
  for each key in new_presidency
    n_previous, average_previous = calculate_average(previous_presidency_suto[key])
    n_new, average_new= calculate_average(new_presidency_suto[key])
    SE_previous = calculate_SE(n_previous, average_previous)
    SE_new = calculate_SE(n_new, average_new)
    z_pooled = calculate_zpooled(SE_previous, SE_new)
    if z_pooled > 2
      append key to statistically_significant_words
  sort(statistically_significant_words)
  significant_words_by_year[year+1] = statistically_signficant_words
  year += 4

write to disk significant_words_by_year
  for each year in in significant_words_by_year
    print signficiant words to line

