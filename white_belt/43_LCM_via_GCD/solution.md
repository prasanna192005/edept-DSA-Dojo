# Solution for Problem 43: LCM via GCD

## Explanation
The LCM can be found using the formula `lcm(a, b) = (|a * b|) / gcd(a, b)`. Use long long to avoid overflow.

---

### C++ Solution
```cpp
#include <iostream>
#include <numeric>

long long gcd(long long a, long long b) {
    while (b) {
        a %= b;
        std::swap(a, b);
    }
    return a;
}

int main() {
    long long a, b;
    std::cin >> a >> b;
    if (a == 0 || b == 0) {
        std::cout << 0 << std::endl;
    } else {
        std::cout << (a * b) / gcd(a, b) << std::endl;
    }
    return 0;
}
```

### Python Solution
```python
import math

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // math.gcd(a, b)

a, b = map(int, input().split())
print(lcm(a, b))
```
