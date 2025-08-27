# Solution for Problem 09: Temperature Conversion

## Explanation
Read the Celsius value and apply the conversion formula. Use floating-point division (`9.0/5.0` or `1.8`) for accuracy.

---

### C++ Solution
```cpp
#include <iostream>
#include <iomanip>

int main() {
    double celsius;
    std::cin >> celsius;
    double fahrenheit = celsius * 9.0 / 5.0 + 32;
    std::cout << std::fixed << std::setprecision(1) << fahrenheit << std::endl;
    return 0;
}
```

### Python Solution
```python
celsius = float(input())
fahrenheit = celsius * 9/5 + 32
print(fahrenheit)
```
