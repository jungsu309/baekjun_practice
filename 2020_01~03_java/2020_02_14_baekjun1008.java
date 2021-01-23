import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        int A,B;
        double result;
        Scanner s = new Scanner(System.in);
        A= s.nextInt();
        B= s.nextInt();//정수 받기
        if (B>0){
        result=A/(double)B;
        System.out.println(result);}
    }
}