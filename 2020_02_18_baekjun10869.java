import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        int a, b;
        Scanner s= new Scanner(System.in);
        a=s.nextInt();
        b=s.nextInt();
        int sum,sub,mul,div,nam;
        System.out.println(sum = a+b);
        System.out.println(sub = a-b);
        System.out.println(mul = a*b);
        System.out.println(div = a/b);
        System.out.println(nam = a%b); 
    }
}