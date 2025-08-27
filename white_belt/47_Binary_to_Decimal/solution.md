# Solution for Problem 47: Binary to Decimal

## Explanation
Iterate through the binary string. For each '1', add `2^power` to the result, where `power` is its position from the right end (starting at 0).

---

### C++ Solution
```cpp
#include <iostream>
#include <string>
#include <cmath>

int main() {
    std::string s;
    std::cin >> s;
    int decimal = 0;
    int power = 0;
    for (int i = s.length() - 1; i >= 0; --i) {
        if (s[i] == '1') {
            decimal += pow(2, power);
        }
        power++;
    }
    std::cout << decimal << std::endl;
    return 0;
}
```

### Python Solution
```python
s = input()
print(int(s, 2))
```
