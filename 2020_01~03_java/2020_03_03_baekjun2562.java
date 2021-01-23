import java.util.Scanner;
import java.util.ArrayList;

public class Main{
    public static void main(String [] args){
        ArrayList <Integer> a = new ArrayList<>();
        Scanner s = new Scanner(System.in);
        int max = 0;//자연수니까 0이라 해도된다.
        int index = 0;//초기화 해주기.
        for(int i=0; i<9; i++){
            int num = s.nextInt();
            a.add(num);//숫자를 넣는중.
            if(max<=a.get(i)){
                max = a.get(i);
                index = i+1;
            }
        }
        System.out.println(max);
        System.out.println(index);
    }
}
