import java.util.*;
public class count_vowels {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in); 
        String s=sc.next(); 
        int c=0; 
        for(char ch:s.toLowerCase().toCharArray())
        { 
            if("aeiou".indexOf(ch)>=0) c++; 
        } 
        System.out.println(c);
    }
}
