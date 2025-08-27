# Solution for Problem 31: String Length

## Explanation
Initialize a counter to 0. Iterate through the characters of the string until you reach the end, incrementing the counter for each character.

---

### C++ Solution
```cpp
#include <iostream>
#include <string>

int main() {
    std::string s;
    std::cin >> s;
    int length = 0;
    for (char c : s) {
        length++;
    }
    std::cout << length << std::endl;
    return 0;
}
```

### Python Solution
```python
s = input()
length = 0
for char in s:
    length += 1
print(length)
```
