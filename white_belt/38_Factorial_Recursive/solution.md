# Solution for Problem 38: Factorial Recursive

## Explanation
The recursive definition of factorial is `fact(n) = n * fact(n-1)`. The base case is `fact(0) = 1`.

---

### C++ Solution
```cpp
#include <iostream>

long long factorial(int n) {
    if (n == 0) {
        return 1;
    }
    return n * factorial(n - 1);
}

int main() {
    int n;
    std::cin >> n;
    std::cout << factorial(n) << std::endl;
    return 0;
}
```

### Python Solution
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input())
print(factorial(n))
```
