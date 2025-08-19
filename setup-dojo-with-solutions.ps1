$base = "edept-dojo-dsa/white-belt"
$problems = @(
    @{num="01"; slug="hello-dojo"; title="Hello Dojo"; desc="Print 'Hello Dojo' to the output."; input="(no input)"; output="Hello Dojo"; 
      c='printf("Hello Dojo\n");'; cpp='cout << "Hello Dojo" << endl;'; java='System.out.println("Hello Dojo");'; js='console.log("Hello Dojo");'; py='print("Hello Dojo")'},
    @{num="02"; slug="sum-of-two"; title="Sum of Two"; desc="Read two integers and print their sum."; input="2 3"; output="5"; 
      c='int a,b; scanf("%d %d",&a,&b); printf("%d\n",a+b);'; cpp='int a,b; cin>>a>>b; cout<<a+b;'; java='Scanner sc=new Scanner(System.in); int a=sc.nextInt(), b=sc.nextInt(); System.out.println(a+b);'; js='const fs=require("fs"); const [a,b]=fs.readFileSync(0,"utf-8").trim().split(/\s+/).map(Number); console.log(a+b);'; py='a,b=map(int,input().split()); print(a+b)'},
    @{num="03"; slug="maximum-of-two"; title="Maximum of Two"; desc="Read two integers and print the maximum."; input="7 4"; output="7"; 
      c='int a,b; scanf("%d %d",&a,&b); printf("%d\n", a>b?a:b);'; cpp='int a,b; cin>>a>>b; cout<<(a>b?a:b);'; java='Scanner sc=new Scanner(System.in); int a=sc.nextInt(), b=sc.nextInt(); System.out.println(Math.max(a,b));'; js='const fs=require("fs"); const [a,b]=fs.readFileSync(0,"utf-8").trim().split(/\s+/).map(Number); console.log(Math.max(a,b));'; py='a,b=map(int,input().split()); print(max(a,b))'},
    @{num="04"; slug="even-or-odd"; title="Even or Odd"; desc="Read an integer and print 'Even' if it is even, otherwise 'Odd'."; input="5"; output="Odd"; 
      c='int n; scanf("%d",&n); printf("%s", (n%2==0)?"Even":"Odd");'; cpp='int n; cin>>n; cout<<(n%2==0?"Even":"Odd");'; java='Scanner sc=new Scanner(System.in); int n=sc.nextInt(); System.out.println(n%2==0?"Even":"Odd");'; js='const fs=require("fs"); const n=+fs.readFileSync(0,"utf-8").trim(); console.log(n%2===0?"Even":"Odd");'; py='n=int(input()); print("Even" if n%2==0 else "Odd")'},
    @{num="05"; slug="sum-of-first-n"; title="Sum of First N"; desc="Read an integer n and print the sum of first n natural numbers."; input="5"; output="15"; 
      c='int n; scanf("%d",&n); printf("%d", n*(n+1)/2);'; cpp='int n; cin>>n; cout<<n*(n+1)/2;'; java='Scanner sc=new Scanner(System.in); int n=sc.nextInt(); System.out.println(n*(n+1)/2);'; js='const fs=require("fs"); const n=+fs.readFileSync(0,"utf-8").trim(); console.log(n*(n+1)/2);'; py='n=int(input()); print(n*(n+1)//2)'},
    @{num="06"; slug="multiplication-table"; title="Multiplication Table"; desc="Read an integer n and print its multiplication table up to 10."; input="3"; output="3 6 9 12 15 18 21 24 27 30"; 
      c='int n; scanf("%d",&n); for(int i=1;i<=10;i++) printf("%d ", n*i);'; cpp='int n; cin>>n; for(int i=1;i<=10;i++) cout<<n*i<<" ";'; java='Scanner sc=new Scanner(System.in); int n=sc.nextInt(); for(int i=1;i<=10;i++) System.out.print(n*i+" ");'; js='const fs=require("fs"); const n=+fs.readFileSync(0,"utf-8").trim(); console.log([...Array(10)].map((_,i)=>n*(i+1)).join(" "));'; py='n=int(input()); print(*[n*i for i in range(1,11)])'},
    @{num="07"; slug="reverse-number"; title="Reverse Number"; desc="Read an integer and print its reverse."; input="1234"; output="4321"; 
      c='int n,rev=0; scanf("%d",&n); while(n){rev=rev*10+n%10;n/=10;} printf("%d",rev);'; cpp='int n,rev=0; cin>>n; while(n){rev=rev*10+n%10;n/=10;} cout<<rev;'; java='Scanner sc=new Scanner(System.in); int n=sc.nextInt(),rev=0; while(n>0){rev=rev*10+n%10;n/=10;} System.out.println(rev);'; js='const fs=require("fs"); let n=fs.readFileSync(0,"utf-8").trim(); console.log(n.split("").reverse().join(""));'; py='n=input().strip(); print(n[::-1])'},
    @{num="08"; slug="palindrome-check"; title="Palindrome Check"; desc="Read a string and print 'Yes' if it is a palindrome, otherwise 'No'."; input="madam"; output="Yes"; 
      c='#include <string.h>\nchar s[100]; scanf("%s",s); int i=0,j=strlen(s)-1,ok=1; while(i<j){ if(s[i++]!=s[j--]) ok=0; } printf(ok?"Yes":"No");'; cpp='string s; cin>>s; string t=s; reverse(t.begin(),t.end()); cout<<(s==t?"Yes":"No");'; java='Scanner sc=new Scanner(System.in); String s=sc.next(); StringBuilder sb=new StringBuilder(s); System.out.println(s.equals(sb.reverse().toString())?"Yes":"No");'; js='const fs=require("fs"); const s=fs.readFileSync(0,"utf-8").trim(); console.log(s===s.split("").reverse().join("")?"Yes":"No");'; py='s=input().strip(); print("Yes" if s==s[::-1] else "No")'},
    @{num="09"; slug="largest-in-array"; title="Largest in Array"; desc="Read n integers and print the largest one."; input="5\n1 7 3 9 2"; output="9"; 
      c='int n; scanf("%d",&n); int a[n]; for(int i=0;i<n;i++) scanf("%d",&a[i]); int mx=a[0]; for(int i=1;i<n;i++) if(a[i]>mx) mx=a[i]; printf("%d",mx);'; cpp='int n; cin>>n; vector<int>a(n); for(int i=0;i<n;i++) cin>>a[i]; cout<<*max_element(a.begin(),a.end());'; java='Scanner sc=new Scanner(System.in); int n=sc.nextInt(); int mx=Integer.MIN_VALUE; for(int i=0;i<n;i++){ int x=sc.nextInt(); if(x>mx) mx=x;} System.out.println(mx);'; js='const fs=require("fs"); const data=fs.readFileSync(0,"utf-8").trim().split(/\s+/).map(Number); const n=data[0], arr=data.slice(1); console.log(Math.max(...arr));'; py='n=int(input()); arr=list(map(int,input().split())); print(max(arr))'},
    @{num="10"; slug="count-vowels"; title="Count Vowels"; desc="Read a string and print the number of vowels in it."; input="hello"; output="2"; 
      c='#include <ctype.h>\nchar s[100]; scanf("%s",s); int c=0; for(int i=0;s[i];i++){ char ch=tolower(s[i]); if(ch==''a''||ch==''e''||ch==''i''||ch==''o''||ch==''u'') c++; } printf("%d",c);'; cpp='string s; cin>>s; int c=0; for(char ch:s){ ch=tolower(ch); if(ch==''a''||ch==''e''||ch==''i''||ch==''o''||ch==''u'') c++; } cout<<c;'; java='Scanner sc=new Scanner(System.in); String s=sc.next(); int c=0; for(char ch:s.toLowerCase().toCharArray()){ if("aeiou".indexOf(ch)>=0) c++; } System.out.println(c);'; js='const fs=require("fs"); const s=fs.readFileSync(0,"utf-8").trim().toLowerCase(); console.log([...s].filter(ch=>"aeiou".includes(ch)).length);'; py='s=input().strip().lower(); print(sum(ch in "aeiou" for ch in s))'}
)

foreach ($p in $problems) {
    $path = "$base/problem-$($p.num)-$($p.slug)"
    New-Item -ItemType Directory -Force -Path $path | Out-Null

    # README.md
    @"
# Problem $($p.num) - $($p.title) (Edept White Belt)

## Problem Statement
$p.desc

### Example
**Input**
$p.input


**Output**
$p.output


### Notes
- This is part of the **Edept Dojo DSA White Belt** problems.
"@ | Set-Content "$path/README.md"

    # Write solutions
    @"
#include <stdio.h>
int main() {
    $($p.c)
    return 0;
}
"@ | Set-Content "$path/$($p.slug).c"

    @"
#include <bits/stdc++.h>
using namespace std;
int main() {
    $($p.cpp)
    return 0;
}
"@ | Set-Content "$path/$($p.slug).cpp"

    @"
import java.util.*;
public class $($p.slug -replace '-', '_') {
    public static void main(String[] args) {
        $($p.java)
    }
}
"@ | Set-Content "$path/$($p.slug).java"

    @"
// Problem $($p.num): $($p.title)
// Edept Dojo
$($p.js)
"@ | Set-Content "$path/$($p.slug).js"

    @"
# Problem $($p.num): $($p.title)
# Edept Dojo
$($p.py)
"@ | Set-Content "$path/$($p.slug).py"
}

Write-Output "✅ All Edept White Belt problems with working solutions created!"