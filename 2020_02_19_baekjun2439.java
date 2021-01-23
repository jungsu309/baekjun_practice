import java.util.Scanner;
public class Main{
    public static void main(String [] args){
        int n;
        Scanner s = new Scanner(System.in);
        n= s.nextInt();
        for (int i=0+1; i<n+1; i++){//5일때
            for(int j=0; j<n-i; j++){//스페이스바 4번
                System.out.printf(" ");
            }
            for (int k=0; k<i; k++){
                System.out.printf("*");
            }
            System.out.printf("\n");
        }
    }
}