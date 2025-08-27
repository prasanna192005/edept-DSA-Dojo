# Solution for Problem 12: Sum of N Natural Numbers

## Explanation
While a loop works, the most efficient method is the mathematical formula: `Sum = N * (N + 1) / 2`.

---

### C++ Solution
```cpp
#include <iostream>

int main() {
    int n;
    std::cin >> n;
    long long sum = (long long)n * (n + 1) / 2;
    std::cout << sum << std::endl;
    return 0;
}
```

### Python Solution
```python
n = int(input())
total_sum = n * (n + 1) // 2
print(total_sum)
```
