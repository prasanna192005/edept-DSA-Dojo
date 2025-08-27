# Solution for Problem 02: Sum of Two

## Explanation
Declare two integer variables, read the values from standard input, and print their sum.

---

### C++ Solution
```cpp
#include <iostream>

int main() {
    int a, b;
    std::cin >> a >> b;
    std::cout << a + b << std::endl;
    return 0;
}
```

### Python Solution
```python
a, b = map(int, input().split())
print(a + b)
```
