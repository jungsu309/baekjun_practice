import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        int A,B,C;
        Scanner s= new Scanner(System.in);
        while(true){
            A = s.nextInt();
            B = s.nextInt();
            C = A+B;
            if(A==0&&B==0){
                break;
            }
            System.out.println(C);
        }
    }
}