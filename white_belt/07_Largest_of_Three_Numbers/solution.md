# Solution for Problem 07: Largest of Three Numbers

## Explanation
Use the built-in `max()` function or nested if-else statements to compare the three numbers.

---

### C++ Solution
```cpp
#include <iostream>
#include <algorithm>

int main() {
    int a, b, c;
    std::cin >> a >> b >> c;
    std::cout << std::max({a, b, c}) << std::endl;
    return 0;
}
```

### Python Solution
```python
a, b, c = map(int, input().split())
print(max(a, b, c))
```
