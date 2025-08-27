# Solution for Problem 36: Count Character Frequency

## Explanation
Initialize a counter to 0. Iterate through the string. If a character in the string matches the target character, increment the counter.

---

### C++ Solution
```cpp
#include <iostream>
#include <string>

int main() {
    std::string s;
    char c;
    std::cin >> s >> c;
    int count = 0;
    for (char ch : s) {
        if (ch == c) {
            count++;
        }
    }
    std::cout << count << std::endl;
    return 0;
}
```

### Python Solution
```python
s = input()
c = input()
print(s.count(c))
```
