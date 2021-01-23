import java.util.*;
public class Main{
    public static void main(String []args){
        Scanner s = new Scanner(System.in);
        int size = s.nextInt();
        int maximum = s.nextInt();
        
        //int arr[]=0;
        ArrayList <Integer> array = new ArrayList<>(); 
        
        for (int i=0; i<size; i++){
            int tmp = s.nextInt();
            if(tmp<maximum){
                array.add(tmp);}//어레이리스트에 넣기.->주어진 숫자보다 작을때만 넣는거야.
        }
        
        
        for (int i=0; i<array.size(); i++){
            System.out.printf(array.get(i)+" ");}
        
    }
}