# Solution for Problem 35: Convert to Uppercase

## Explanation
Iterate through the string. For each character, convert it to its uppercase equivalent. Most languages provide a built-in function for this.

---

### C++ Solution
```cpp
#include <iostream>
#include <string>
#include <cctype>

int main() {
    std::string s;
    std::cin >> s;
    for (char &c : s) {
        c = toupper(c);
    }
    std::cout << s << std::endl;
    return 0;
}
```

### Python Solution
```python
s = input()
print(s.upper())
```
