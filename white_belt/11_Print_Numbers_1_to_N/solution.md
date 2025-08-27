# Solution for Problem 11: Print Numbers 1 to N

## Explanation
Use a `for` loop that initializes a counter at 1, continues as long as the counter is less than or equal to `N`, and increments by 1.

---

### C++ Solution
```cpp
#include <iostream>

int main() {
    int n;
    std::cin >> n;
    for (int i = 1; i <= n; ++i) {
        std::cout << i << std::endl;
    }
    return 0;
}
```

### Python Solution
```python
n = int(input())
for i in range(1, n + 1):
    print(i)
```
