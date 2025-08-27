# Solution for Problem 32: Reverse a String

## Explanation
Iterate through the string from the last character to the first and append each character to a new string. Python's slicing `[::-1]` is a convenient shortcut.

---

### C++ Solution
```cpp
#include <iostream>
#include <string>
#include <algorithm>

int main() {
    std::string s;
    std::cin >> s;
    std::reverse(s.begin(), s.end());
    std::cout << s << std::endl;
    return 0;
}
```

### Python Solution
```python
s = input()
print(s[::-1])
```
