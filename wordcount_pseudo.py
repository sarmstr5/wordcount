1) Graph runtime of wordcount with varying size datasets
Class map(string s)
  Split string into words
    for each word
      Emit(string word, int 1)

Class reducer(string s, int i)
  s_count = 0
  for each string s
    s_count = s_count + i
  end for
  Emit(sting s, s_count)

2) Remove html and punction
Class parse_website(string url)
  page_text = ''
  html = Query_website(url)
  for each paragraph tag in html
    Append paragraph text to page_text  
  end for
  for each char in page_text
    if char is a punction mark
      remove char
    end if
  end for

3) Count average word in address
Class map(string s)
  Split string into words
  for each word
    Emit(word, 1)
  end for
    
Class reducer(string word, int i)
  sum = 0
  word_dictionary = new hashtable
  
  while stdin is not empty
    if word is in word_dictionary
      Increment word_dictionary[word] by i
    end if
    else
      Append word to word_dictionary
      Increment word_dictionary[word] by i
    end else
    Increment sum by i
  end while
  Emit(word, word_dictionary[word]/sum)


4) compute max and min a word appears in all addresses
class max_min_map()
  address_count = 0
  word_dictionary = new hashtable
  for each address in addresses
    Increment address_count
    for each line in address
      for each word in line
        if word is in word_dictionary
          Increment word count in word_dictionary
        end if
        else
          Append word to word_dictionary
          Increment word count in word_dictionary
        end else
      end for
    end for
      for each word in word_dictionary
        Emit(<address_count, [word, word count]>)
    word_dictionary = new hashtable
  end for

Class max_min_wc_reduce(integer address_id, string word, int count))
  sum = 0
  max_min_dictionary = new hashtable
  current_dictionary = new hashtable
  
  while stdin is not empty
    for each address_id
      for each word
        if word is in current_dictionary
          Increment word_dictionary[word] by i
        end if
        else
          Append word to word_dictionary
          Increment word_dictionary[word] by i
        end else
      end for
      for each word in current_dictionary
        if word is in max_min_dictionary
          Increment max_min_dictionary[word] by i
        end if
        else
          Append word to max_min_dictionary
          Increment max_min_dictionary[word] by i
  end while
  for each word, counts in max_min_dictionary
    max = max(counts)
    min = min(counts)
    Emit(word, max, min))

5) Compute avg and std of words in 4 year windows from 1985

class window_avg_map()
  window = 4
  year = 0
  partition = 0
  word_dictionary = new hashtable

  for each address in addresses
    for each line in address
      for each word in line
        if year and word is in word_dictionary
          Incremnt that years word count in word_dictionary
        end if
        else
          Append word to word_dictionary
          Increment that years word count in word_dictionary
        end else
      end for
      if year == window
        for string word, list counts in word_dictionary
          Emit(<partition, [word, counts]>)
        word_dictionary = new hashtable
        Increment partition
        year = 0
    end for
    Increment year
  end for

class window_avg_reducer(int partition, string word, list counts)
  start_year = 1985
  end_year = start_year + partition * 4
  word_dictionary = new hashtable
  for part in partition
    for each word
      if  word is in word_dictionary
        Increment year1, year2, year3, year4, year5 by counts
      end if
      else
        Append word to word_dictionary
        Increment year1, year2, year3, year4, year5 by counts
      end else
    Calculate avg
    Calculate std
    Enit(<(start_year,end_year), word, std, avg>))
      

6) In post window years, find words whose use was greater than 2 stds (e.g. 89)
6.a) post window years
6.b) find statstically significant words
class window_avg_map()
  window = 4
  year = 0
  partition = 0
  word_dictionary = new hashtable

  for each address in addresses
  if year > 0
    continue
    for each line in address
      for each word in line
        if year==0 and word is in word_dictionary
          Incremnt that years word count in word_dictionary
        end if
        else
          Append word to word_dictionary
          Increment that years word count in word_dictionary
        end else
      end for
      if year == window
        for string word, list counts in word_dictionary
          Emit(<partition, [word, counts]>)
        word_dictionary = new hashtable
        Increment partition
        year = 0
    end for
    Increment year
  end for

# from stdin will recieve a partition number, word, and list of 5 word counts 
# where each word count is year0, year1, year2, year3 and the new term
class window_avg_reducer(int partitions, string word, list counts)
  start_year = 1985
  end_year = start_year + partition * 4
  word_dictionary = new hashtable

  # the keys were emitted by partition so they will be sorted in that way
  # each partition represents the presidential term
  for each part in partition
    for each word
      if  word is in word_dictionary
        Increment year1, year2, year3, year4, year5 by counts
      end if
      else
        Append word to word_dictionary
        Increment year1, year2, year3, year4, year5 by counts
      end else
    for each word from term
      Calculate avg for first 4 counts
      Calculate std between first 4 counnts and last count
    end for
    if std > 2
      Enit(<(start_year,end_year), word, std, avg>)
    end if
    year = start_year + 4

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


year = start_year
while year < 2018
  term_year = 0
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
