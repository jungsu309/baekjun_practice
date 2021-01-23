import java.util.*;
import java.io.*;
public class Main{
    public static void main(String []args) throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in)); //선언
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s = bf.readLine();
        int size = Integer.parseInt(s);//여기에 횟수 들어있을 것.
        for (int i = 0; i < size; i++){
            String readString = bf.readLine();
            String[] splitArray = readString.split(" ");
            int[] intArray = Arrays.stream(splitArray).mapToInt(Integer::parseInt).toArray();
            int sum = intArray[0]+intArray[1];//두개 더해.
            bw.write(sum+"\n");
        }
        bw.flush();
        bw.close();
    }
}