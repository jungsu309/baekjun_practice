import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;

public class Main{
    public static void main(String[] args){
        ArrayList<Integer> al = new ArrayList<>();
        int N, max, min;
        Scanner s= new Scanner(System.in);
        N = s.nextInt();
        int i=0;
        while(i <N){
            int k;
            k = s.nextInt();
            al.add(k);// 누적으로 쌓였으면 좋겠다.
            i++;
        }//갯수만큼 잘 입력되있는 어레이리스트 준비 됨.
        max = al.get(0);
        min = al.get(0);//둘에게 가장 처음 값 넣어준다.
        
        for (int j =0; j<N; j++){
            if (max<al.get(j)){//다른수가 더 큰경우
                max = al.get(j);
            }
            if (min>al.get(j)){//다른수가 더 작은경우
                min = al.get(j);
            }        
        }
        
        System.out.println(min+" "+ max);
    }
}