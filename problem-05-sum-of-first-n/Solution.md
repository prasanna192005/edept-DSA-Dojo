### C Solution

```c
#include <stdio.h>
int main() {
    int n; 
    scanf("%d",&n); 
    printf("%d", n*(n+1)/2);
    return 0;
}
```

### C++ Solution

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n; 
    cin>>n; 
    cout<<n*(n+1)/2;
    return 0;
}
```

### Java Solution

```java
import java.util.*;
public class sum_of_first_n {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in); 
        int n=sc.nextInt(); 
        System.out.println(n*(n+1)/2);
    }
}
```

### Python Solution

```python
# Problem 05: Sum of First N
# Edept Dojo
n=int(input()); 
print(n*(n+1)//2)
```

### Javascript Solution

```javascript
// Problem 05: Sum of First N
// Edept Dojo
const fs=require("fs"); 
const n=+fs.readFileSync(0,"utf-8").trim(); 
console.log(n*(n+1)/2);
```
