# Solution for Problem 50: Print Fibonacci Series

## Explanation
Initialize two variables, `a=0` and `b=1`. Loop `N` times. In each iteration, print `a`, then calculate the next term `c = a + b`, and update `a` to `b` and `b` to `c`.

---

### C++ Solution
```cpp
#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    long long a = 0, b = 1;
    for (int i = 0; i < n; ++i) {
        std::cout << a << (i == n - 1 ? "" : " ");
        long long next = a + b;
        a = b;
        b = next;
    }
    std::cout << std::endl;
    return 0;
}
```

### Python Solution
```python
n = int(input())
a, b = 0, 1
result = []
for _ in range(n):
    result.append(a)
    a, b = b, a + b
print(*result)
```
