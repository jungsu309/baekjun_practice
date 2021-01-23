import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        int H,M;
        Scanner s= new Scanner(System.in);
        H=s.nextInt();
        M=s.nextInt();
        if (M<45&&M>=0){
            if(H==0){//자정이면 23시로 바꿔야된다. 1시간을 60분으로 넘긴다음에 계산해주기
                H=23;
                M=60+M-45;
            }
            else{
                H=H-1;
                M=60+M-45;
            }
        }
        else if(M>=45&&M<=60){
            M=M+-45;//그냥 45분 빼기
        }
        System.out.println(H+" "+M);
    }
}