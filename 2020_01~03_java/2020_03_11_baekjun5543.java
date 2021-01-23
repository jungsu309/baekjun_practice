import java.util.*;
public class Main{
    public static void main(String []args){
        Scanner s = new Scanner(System.in);
        int bugger1 = s.nextInt();
        int bugger2 = s.nextInt();
        int bugger3 = s.nextInt();
        int drink1 = s.nextInt();
        int drink2 = s.nextInt();
        
        int b_min=0;
        if (bugger1<=bugger2&&bugger1<=bugger3){
            b_min = bugger1;
        }
        else if(bugger2<=bugger1&& bugger2<=bugger3){
            b_min =bugger2;
        }
        else{
            b_min = bugger3;
        }
        int d_min=0;
        if(drink1>=drink2){
            d_min = drink2;
        }
        else{
            d_min=drink1;
        }//음료비교
        int answer = b_min+d_min-50;
        System.out.println(answer);
    }
}