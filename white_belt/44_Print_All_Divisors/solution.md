# Solution for Problem 44: Print All Divisors

## Explanation
Iterate from 1 up to `N`. If `N` is divisible by the current number `i`, then `i` is a divisor.

---

### C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;
    for (int i = 1; i <= n; ++i) {
        if (n % i == 0) {
            std::cout << i << " ";
        }
    }
    std::cout << std::endl;
    return 0;
}
```

### Python Solution
```python
n = int(input())
divisors = []
for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
print(*divisors)
```
