### C Solution

```c
#include <stdio.h>
#include <string.h>
int main() {
    char s[100]; 
    scanf("%s",s); 
    int i=0,j=strlen(s)-1,ok=1; 
    while(i<j){ if(s[i++]!=s[j--]) ok=0; } 
    printf(ok?"Yes":"No");
    return 0;
}
```

### C++ Solution

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    string s; 
    cin>>s; 
    string t=s; 
    reverse(t.begin(),t.end()); 
    cout<<(s==t?"Yes":"No");
    return 0;
}
```

### Java Solution

```java
import java.util.*;
public class palindrome_check {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in); 
        String s=sc.next(); 
        StringBuilder sb=new StringBuilder(s); 
        System.out.println(s.equals(sb.reverse().toString())?"Yes":"No");
    }
}
```

### Python Solution

```python
# Problem 08: Palindrome Check
# Edept Dojo
s=input().strip(); 
print("Yes" if s==s[::-1] else "No")
```

### Javascript Solution

```javascript
// Problem 08: Palindrome Check
// Edept Dojo
const fs=require("fs"); 
const s=fs.readFileSync(0,"utf-8").trim(); 
console.log(s===s.split("").reverse().join("")?"Yes":"No");
```
