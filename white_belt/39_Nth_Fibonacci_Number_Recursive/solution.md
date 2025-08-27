# Solution for Problem 39: Nth Fibonacci Number Recursive

## Explanation
The recursive formula is `fib(n) = fib(n-1) + fib(n-2)`. The base cases are `fib(0) = 0` and `fib(1) = 1`. This approach is very slow due to repeated calculations.

---

### C++ Solution
```cpp
#include <iostream>

int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int n;
    std::cin >> n;
    std::cout << fibonacci(n) << std::endl;
    return 0;
}
```

### Python Solution
```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())
print(fibonacci(n))
```
