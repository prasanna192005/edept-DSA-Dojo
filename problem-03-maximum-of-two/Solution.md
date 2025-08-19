### C Solution

```c
#include <stdio.h>
int main() {
    int a,b; 
    scanf("%d %d",&a,&b); 
    printf("%d\n", a>b?a:b);
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
    cout<<(a>b?a:b);
    return 0;
}
```

### Java Solution

```java
import java.util.*;
public class maximum_of_two {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in); 
        int a=sc.nextInt(), b=sc.nextInt();
        System.out.println(Math.max(a,b));
    }
}
```

### Python Solution

```python
# Problem 03: Maximum of Two
# Edept Dojo
a,b=map(int,input().split()); 
print(max(a,b))
```

### Javascript Solution

```javascript
// Problem 03: Maximum of Two
// Edept Dojo
const fs=require("fs");
const [a,b]=fs.readFileSync(0,"utf-8").trim().split(/\s+/).map(Number);
console.log(Math.max(a,b));
```
