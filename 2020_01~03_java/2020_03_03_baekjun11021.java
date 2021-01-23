import java.util.Scanner;
public class Main{
    public static void main(String [] args){
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        for(int i=0+1; i<n+1; i++){
            int a = s.nextInt();
            int b = s.nextInt();
            int sum = a+b;
            System.out.println("Case #"+i+": "+sum);
        }
    }
}