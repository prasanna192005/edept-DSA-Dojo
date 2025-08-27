# Solution for Problem 19: Print Even Numbers

## Explanation
Loop from 1 to `N`. Inside the loop, check if the current number is divisible by 2. If it is, print it.

---

### C++ Solution
```cpp
#include <iostream>

int main() {
    int n;
    std::cin >> n;
    for (int i = 1; i <= n; ++i) {
        if (i % 2 == 0) {
            std::cout << i << std::endl;
        }
    }
    return 0;
}
```

### Python Solution
```python
n = int(input())
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)
```
