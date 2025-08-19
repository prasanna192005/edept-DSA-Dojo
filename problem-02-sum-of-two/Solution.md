### C Solution

```c
#include <stdio.h>
int main() {
    int a,b; 
    scanf("%d %d",&a,&b); 
    printf("%d\n",a+b);
    return 0;
}
```

### C++ Solution

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    int a,b; 
    cin>>a>>b; 
    cout<<a+b;
    return 0;
}
```

### Java Solution

```java
import java.util.*;
public class sum_of_two {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in); 
        int a=sc.nextInt(), b=sc.nextInt(); 
        System.out.println(a+b);
    }
}
```

### Python Solution

```python
# Problem 02: Sum of Two
# Edept Dojo
a,b=map(int,input().split()); 
print(a+b)
```

### Javascript Solution

```javascript
// Problem 02: Sum of Two
// Edept Dojo
const fs=require("fs"); 
const [a,b]=fs.readFileSync(0,"utf-8").trim().split(/\s+/).map(Number); 
console.log(a+b);
```
