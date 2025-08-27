# Solution for Problem 18: Power of a Number

## Explanation
Initialize a result to 1. Use a loop that runs `exponent` times, multiplying the result by the `base` in each iteration.

---

### C++ Solution
```cpp
#include <iostream>

int main() {
    int base, exponent;
    std::cin >> base >> exponent;
    long long result = 1;
    for (int i = 0; i < exponent; ++i) {
        result *= base;
    }
    std::cout << result << std::endl;
    return 0;
}
```

### Python Solution
```python
base, exponent = map(int, input().split())
result = 1
for _ in range(exponent):
    result *= base
print(result)
```
