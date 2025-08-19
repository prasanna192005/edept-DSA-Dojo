### C Solution

```c
#include <stdio.h>
int main() {
    int n; scanf("%d",&n); 
    int a[n]; 
    for(int i=0;i<n;i++) scanf("%d",&a[i]); 
    int mx=a[0]; 
    for(int i=1;i<n;i++) if(a[i]>mx) mx=a[i]; 
    printf("%d",mx);
    return 0;
}
```

### C++ Solution

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n; cin>>n; 
    vector<int>a(n); 
    for(int i=0;i<n;i++) cin>>a[i]; 
    cout<<*max_element(a.begin(),a.end());
    return 0;
}
```

### Java Solution

```java
import java.util.*;
public class largest_in_array {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in); 
        int n=sc.nextInt(); 
        int mx=Integer.MIN_VALUE; 
        for(int i=0;i<n;i++){ 
            int x=sc.nextInt(); 
            if(x>mx) mx=x;
        } 
        System.out.println(mx);
    }
}
```

### Python Solution

```python
# Problem 09: Largest in Array
# Edept Dojo
n=int(input());
arr=list(map(int,input().split()));
print(max(arr))
```

### Javascript Solution

```javascript
// Problem 09: Largest in Array
// Edept Dojo
const fs=require("fs"); 
const data=fs.readFileSync(0,"utf-8").trim().split(/\s+/).map(Number); 
const n=data[0], arr=data.slice(1); 
console.log(Math.max(...arr));
```
