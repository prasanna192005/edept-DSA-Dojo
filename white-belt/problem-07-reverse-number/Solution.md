### C Solution

```c
#include <stdio.h>
int main() {
    int n,rev=0; 
    scanf("%d",&n); 
    while(n){
        rev=rev*10+n%10;
        n/=10;
    } 
    printf("%d",rev);
    return 0;
}
```

### C++ Solution

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n,rev=0; 
    cin>>n; 
    while(n){
        rev=rev*10+n%10;
        n/=10;
    } 
    cout<<rev;
    return 0;
}
```

### Java Solution

```java
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
```

### Python Solution

```python
# Problem 07: Reverse Number
# Edept Dojo
n=input().strip();
print(n[::-1])
```

### Javascript Solution

```javascript
// Problem 07: Reverse Number
// Edept Dojo
const fs=require("fs"); 
let n=fs.readFileSync(0,"utf-8").trim(); 
console.log(n.split("").reverse().join(""));
```
