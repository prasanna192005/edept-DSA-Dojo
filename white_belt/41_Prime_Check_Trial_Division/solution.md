# Solution for Problem 41: Prime Check Trial Division

## Explanation
A prime number is greater than 1 and has no divisors other than 1 and itself. Iterate from 2 up to the square root of `N`. If `N` is divisible by any number in this range, it's not prime.

---

### C++ Solution
```cpp
#include <iostream>
#include <cmath>

int main() {
    int n;
    std::cin >> n;
    bool is_prime = true;
    if (n <= 1) {
        is_prime = false;
    } else {
        for (int i = 2; i * i <= n; ++i) {
            if (n % i == 0) {
                is_prime = false;
                break;
            }
        }
    }
    if (is_prime) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "No" << std::endl;
    }
    return 0;
}
```

### Python Solution
```python
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
if is_prime(n):
    print("Yes")
else:
    print("No")
```
