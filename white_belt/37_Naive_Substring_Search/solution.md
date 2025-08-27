# Solution for Problem 37: Naive Substring Search

## Explanation
Iterate through the `text` with an index `i`. For each `i`, check if the substring of `text` starting at `i` with the length of `pattern` is equal to `pattern`.

---

### C++ Solution
```cpp
#include <iostream>
#include <string>

int main() {
    std::string text, pattern;
    std::cin >> text >> pattern;
    size_t found = text.find(pattern);
    if (found != std::string::npos) {
        std::cout << found << std::endl;
    } else {
        std::cout << -1 << std::endl;
    }
    return 0;
}
```

### Python Solution
```python
text = input()
pattern = input()
print(text.find(pattern))
```
