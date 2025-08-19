### C Solution

```c
#include <stdio.h>
int main() {
    int n; scanf("%d",&n); 
    for(int i=1;i<=10;i++) printf("%d ", n*i);
    return 0;
}
```

### C++ Solution

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n; cin>>n; 
    for(int i=1;i<=10;i++) {
        cout<<n*i<<" ";
    }
    return 0;
}
```

### Java Solution

```java
import java.util.*;
public class multiplication_table {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in); 
        int n=sc.nextInt(); 
        for(int i=1;i<=10;i++) {
            System.out.print(n*i+" ");
        }
    }
}
```

### Python Solution

```python
# Problem 06: Multiplication Table
# Edept Dojo
n=int(input()); 
print(*[n*i for i in range(1,11)])
```

### Javascript Solution

```javascript
// Problem 06: Multiplication Table
// Edept Dojo
const fs=require("fs"); 
const n=+fs.readFileSync(0,"utf-8").trim(); 
console.log([...Array(10)].map((_,i)=>n*(i+1)).join(" "));
```
