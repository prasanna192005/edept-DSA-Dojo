# Solution for Problem 10: Swap Two Numbers

## Explanation
Use a third temporary variable to hold one value while you perform the swap. Python allows for direct tuple assignment `a, b = b, a`.

---

### C++ Solution
```cpp
#include <iostream>

int main() {
    int a, b;
    std::cin >> a >> b;
    int temp = a;
    a = b;
    b = temp;
    std::cout << a << " " << b << std::endl;
    return 0;
}
```

### Python Solution
```python
a, b = map(int, input().split())
a, b = b, a
print(a, b)
```
