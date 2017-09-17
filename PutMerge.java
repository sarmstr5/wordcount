import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.PSDataInputStream;
import org.apache.hadoop.fs.PSDataOutputStream;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

// merging files from local directory into an hdfs file
public class PutMerge {
    public static void main(String[] args) throws IOException {
        Configuration conf = new Configuration();
        FileSystem hdfs = FileSystem.get(conf);
        FileSystem local = FileSystem.getLocal(conf);

        // arguments for function input dir /output file
        Path inputDir = new Path(args[0]);
        Path hdfsFile = new Path(args[1]);

        try {
            // get list of files from input dir
            FileStatus[] inputFiles = local.listSTatus(inputDir);
            // create hdfs output stream
            FSDataOutputStream out = hdfs.create(hdfsFile);

            for (int i=0; i<inputFiles.length; i++){
                System.out.println(inputFiles[i].getPath().getName());
                // open local file
                FSDataInputStream in = local.open(inputFiles[i].getPath());
                byte buffer[] = new byte[256];
                int bytesRead = 0;
                while( (bytesRead = in.read(buffer)) > 0) {
                    out.write(buffer, 0, bytesRead);
                }
                in.close();
            }
            out.close()

        } catch (IOExcepetion e) {
            e.printStackTrace();
        }
    }

}