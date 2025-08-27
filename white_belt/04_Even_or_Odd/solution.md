# Solution for Problem 04: Even or Odd

## Explanation
An integer is even if it's perfectly divisible by 2. Use the modulo operator (`%`). If `N % 2` is 0, it's even.

---

### C++ Solution
```cpp
#include <iostream>

int main() {
    int n;
    std::cin >> n;
    if (n % 2 == 0) {
        std::cout << "Even" << std::endl;
    } else {
        std::cout << "Odd" << std::endl;
    }
    return 0;
}
```

### Python Solution
```python
n = int(input())
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
```
