# Solution for Problem 33: Check for Palindrome

## Explanation
A simple way is to compare the original string with its reversed version. If they are the same, it's a palindrome.

---

### C++ Solution
```cpp
#include <iostream>
#include <string>
#include <algorithm>

int main() {
    std::string s;
    std::cin >> s;
    std::string reversed_s = s;
    std::reverse(reversed_s.begin(), reversed_s.end());
    if (s == reversed_s) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "No" << std::endl;
    }
    return 0;
}
```

### Python Solution
```python
s = input()
if s == s[::-1]:
    print("Yes")
else:
    print("No")
```
