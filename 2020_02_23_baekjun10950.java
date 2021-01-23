import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        int A,B,C,D;
        Scanner s= new Scanner(System.in);
        A = s.nextInt();
        for(int i=0; i<A; i++){
            B = s.nextInt();
            C = s.nextInt();
            D = B+C;
            System.out.println(D);
        }
    }
}