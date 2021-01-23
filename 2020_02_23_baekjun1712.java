import java.util.Scanner;
public class Main{
    public static void main(String [] args){
        int A, B;//A=고정비용->항상들어가는비용, B = 가변비용->한대마다 들어가는 비용 
        int C;//= 한대가격.
        //21억 이하의 자연수를 갖게끔 앞에 형 바꿔주자.
        //if(n대의 컴퓨터*C>=A+n대의 컴퓨터*B){손익분기점.-n출력}
        Scanner s= new Scanner(System.in);
        A = s.nextInt();//int라고 해도 될까?
        B = s.nextInt();
        C = s.nextInt();
        
        //식 = A+n*B<n*C 정리하면 A/(C-B)<n이니까 A/(C-B) +1 해주면 된다
        //손익 분기점이 나지 않을때->c<b일때? A가 0이라 해도 절대 넘지 못하니까.
        
        if(C<=B){
            
            System.out.println("-1");
        }
        else{
            System.out.println((A/(C-B))+1);
            
        }
          
        
    }
}