public class WordCount extends Configured implements Tool {
  public static class MapClass extends MapReduceBase implements Mapper<Longwritable, Text, Text, IntWritable> {
    private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();

    // processes one line at a time
    public void map(LongWritable key, Text value, OutputCollector<Text, IntWritable> output, Reporter reporter) throws IOException {
      String line = value.toString();

      // Tokenize using white space
      StringTokenizer iter = new StringTokenizer(line, " \t\n\r\f,.:;?![]'");
      while(itr.hasMoreTokens()) {
        // Cast token into Text Object
        word.set(iter.nextToken().toLowerCase());
        // <key == word, 1>
        output.collect(word, one);
      }
   }
  }

  public static class Reduce extends MapReduceBase implements Reduce<Text, IntWritable, Text, IntWritable>{
    public void reduce(Text key, Iterator<IntWritable> values, OutputCollector<Text, IntWritable> output, Reporter reporter) throws IOException {
      int sum = 0;
      while(values.hasNext()) {
        sum += values.next().get();
      }
      // output each token
      output.collect(key, new IntWritable(sum));
    }
  }
}

