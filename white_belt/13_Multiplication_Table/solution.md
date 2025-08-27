# Solution for Problem 13: Multiplication Table

## Explanation
Use a `for` loop that iterates from 1 to 10. In each iteration, print the formatted string with the product.

---

### C++ Solution
```cpp
#include <iostream>

int main() {
    int n;
    std::cin >> n;
    for (int i = 1; i <= 10; ++i) {
        std::cout << n << " x " << i << " = " << n * i << std::endl;
    }
    return 0;
}
```

### Python Solution
```python
n = int(input())
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```
