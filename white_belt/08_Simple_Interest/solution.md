# Solution for Problem 08: Simple Interest

## Explanation
Read the inputs and apply the formula. Use floating-point variables for calculation to ensure precision.

---

### C++ Solution
```cpp
#include <iostream>
#include <iomanip>

int main() {
    int p, t;
    double r;
    std::cin >> p >> r >> t;
    double si = (p * r * t) / 100.0;
    std::cout << std::fixed << std::setprecision(1) << si << std::endl;
    return 0;
}
```

### Python Solution
```python
p_str, r_str, t_str = input().split()
p = int(p_str)
r = float(r_str)
t = int(t_str)
si = (p * r * t) / 100
print(si)
```
