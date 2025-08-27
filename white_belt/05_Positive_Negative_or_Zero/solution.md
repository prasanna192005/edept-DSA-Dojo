# Solution for Problem 05: Positive Negative or Zero

## Explanation
Use an if-elif-else structure. If `N > 0`, it's positive. If `N < 0`, it's negative. Otherwise, it's zero.

---

### C++ Solution
```cpp
#include <iostream>

int main() {
    int n;
    std::cin >> n;
    if (n > 0) {
        std::cout << "Positive" << std::endl;
    } else if (n < 0) {
        std::cout << "Negative" << std::endl;
    } else {
        std::cout << "Zero" << std::endl;
    }
    return 0;
}
```

### Python Solution
```python
n = int(input())
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
```
