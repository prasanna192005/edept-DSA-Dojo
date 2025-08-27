# Solution for Problem 42: GCD Euclidean Algorithm

## Explanation
The Euclidean algorithm states that `gcd(a, b)` is the same as `gcd(b, a % b)`. The base case is when `b` is 0, at which point the GCD is `a`.

---

### C++ Solution
```cpp
#include <iostream>

int gcd(int a, int b) {
    while (b) {
        a %= b;
        std::swap(a, b);
    }
    return a;
}

int main() {
    int a, b;
    std::cin >> a >> b;
    std::cout << gcd(a, b) << std::endl;
    return 0;
}
```

### Python Solution
```python
import math

a, b = map(int, input().split())
print(math.gcd(a, b))
```
