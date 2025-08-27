# Solution for Problem 46: Decimal to Binary

## Explanation
Repeatedly take the number modulo 2 to get the next binary digit, then divide the number by 2. Build the string of digits, then reverse it.

---

### C++ Solution
```cpp
#include <iostream>
#include <string>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;
    if (n == 0) {
        std::cout << "0" << std::endl;
        return 0;
    }
    std::string binary = "";
    while (n > 0) {
        binary += std::to_string(n % 2);
        n /= 2;
    }
    std::reverse(binary.begin(), binary.end());
    std::cout << binary << std::endl;
    return 0;
}
```

### Python Solution
```python
n = int(input())
print(bin(n)[2:])
```
