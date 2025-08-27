# Solution for Problem 20: Simple Star Pattern

## Explanation
Use nested loops. The outer loop will run `N` times for each row. The inner loop will run `i` times (where `i` is the current row number) to print the stars.

---

### C++ Solution
```cpp
#include <iostream>

int main() {
    int n;
    std::cin >> n;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= i; ++j) {
            std::cout << "*";
        }
        std::cout << std::endl;
    }
    return 0;
}
```

### Python Solution
```python
n = int(input())
for i in range(1, n + 1):
    print('*' * i)
```
