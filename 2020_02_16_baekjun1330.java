import java.util.Scanner;
public class Main{
    public static void main (String[] args){
        int A,B;
        Scanner s = new Scanner(System.in);
        A= s.nextInt();
        B= s.nextInt();//정수 받기
        
        if(A>B){
            System.out.printf(">");
        }
        else if (A<B){
            System.out.printf("<");
        }
        else{
            System.out.printf("==");}
    }
}