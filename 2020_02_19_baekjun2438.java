import java.util.Scanner;
public class Main {
    public static void main(String [] args){
        int n;
        Scanner s= new Scanner(System.in);
        n = s.nextInt();//5 입력시
        for (int i=0; i<n; i++){//일단 0부터 시작
            for (int j=0; j<i+1; j++){
                System.out.printf("*");
            }
            System.out.printf("\n");
        }
    }
}