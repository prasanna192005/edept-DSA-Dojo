import java.util.*;
public class reverse_number {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
         int n=sc.nextInt(),rev=0; 
         while(n>0)
         {
             rev=rev*10+n%10;
             n/=10;
         } 
         System.out.println(rev);
    }
}
