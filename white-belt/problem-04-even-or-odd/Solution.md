### C Solution

```c
#include <stdio.h>
int main() {
    int n; 
    scanf("%d",&n); 
    printf("%s", (n%2==0)?"Even":"Odd");
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
    cout<<(n%2==0?"Even":"Odd");
    return 0;
}
```

### Java Solution

```java
import java.util.*;
public class even_or_odd {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in); 
        int n=sc.nextInt(); 
        System.out.println(n%2==0?"Even":"Odd");
    }
}
```

### Python Solution

```python
# Problem 04: Even or Odd
# Edept Dojo
n=int(input());
print("Even" if n%2==0 else "Odd")
```

### Javascript Solution

```javascript
// Problem 04: Even or Odd
// Edept Dojo
const fs=require("fs"); 
const n=+fs.readFileSync(0,"utf-8").trim(); 
console.log(n%2===0?"Even":"Odd");
```
