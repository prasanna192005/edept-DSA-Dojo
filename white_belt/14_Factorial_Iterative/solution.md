# Solution for Problem 14: Factorial Iterative

## Explanation
Initialize a result variable to 1. Loop from 1 to N, multiplying the result by the loop counter in each step. Factorial of 0 is 1.

---

### C++ Solution
```cpp
#include <iostream>

int main() {
    int n;
    std::cin >> n;
    long long factorial = 1;
    for (int i = 1; i <= n; ++i) {
        factorial *= i;
    }
    std::cout << factorial << std::endl;
    return 0;
}
```

### Python Solution
```python
n = int(input())
factorial = 1
if n < 0:
    print("Factorial does not exist for negative numbers")
elif n == 0:
    print(1)
else:
    for i in range(1, n + 1):
        factorial = factorial * i
    print(factorial)
```
