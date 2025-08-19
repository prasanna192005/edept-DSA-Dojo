### C Solution

```c
#include <stdio.h>
#include <ctype.h>
int main() {
    char s[100]; scanf("%s",s); 
    int c=0; 
    for(int i=0;s[i];i++)
    { 
        char ch=tolower(s[i]);
        if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u') c++; 
    } 
    printf("%d",c);
    return 0;
}
```

### C++ Solution

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    string s; cin>>s; 
    int c=0; for(char ch:s)
    { 
        ch=tolower(ch); 
        if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u') c++; 
    } cout<<c;
    return 0;
}
```

### Java Solution

```java
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
```

### Python Solution

```python
# Problem 10: Count Vowels
# Edept Dojo
s=input().strip().lower(); 
print(sum(ch in "aeiou" for ch in s))
```

### Javascript Solution

```javascript
// Problem 10: Count Vowels
// Edept Dojo
const fs=require("fs");
const s=fs.readFileSync(0,"utf-8").trim().toLowerCase();
console.log([...s].filter(ch=>"aeiou".includes(ch)).length);
```
