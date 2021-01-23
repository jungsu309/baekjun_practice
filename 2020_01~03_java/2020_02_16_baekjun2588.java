import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        int n1, n2;
        Scanner s = new Scanner(System.in);
        n1 = s.nextInt();
        n2 = s.nextInt();//입력받기
        
        //n2 = 432일경우
        
        
        int n2_100, n2_10, n2_1;//자릿수 추출하기
        n2_100 = n2/100;//100의 자리 숫자 432나누기 100 의 몫=4
        n2_10 = (n2%100)/10;//10의자리 숫자 432나누기 100의 나머지->32를 10으로 나눈 값의 몫=3
        n2_1 = (n2%100)%10;//1의자리 숫자432를 100으로 나눈나머지=32를 다시 10으로 나눈값의 나머지=2
        int n3, n4, n5, n6;//각자 출력하고 싶은 자리
        n3 = n1*n2_1;
        n4 = n1*n2_10;
        n5 = n1*n2_100;
        n6 =n1*n2;
        System.out.println(n3+"\n"+n4+"\n"+n5+"\n"+n6);
    }
}