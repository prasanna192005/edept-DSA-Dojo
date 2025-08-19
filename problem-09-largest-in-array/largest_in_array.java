import java.util.*;
public class largest_in_array {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in); 
        int n=sc.nextInt(); 
        int mx=Integer.MIN_VALUE; 
        for(int i=0;i<n;i++){ 
            int x=sc.nextInt(); 
            if(x>mx) mx=x;
        } 
        System.out.println(mx);
    }
}
