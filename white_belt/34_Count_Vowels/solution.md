# Solution for Problem 34: Count Vowels

## Explanation
Initialize a counter to 0. Iterate through each character of the string. Convert the character to lowercase and check if it is 'a', 'e', 'i', 'o', or 'u'. If it is, increment the counter.

---

### C++ Solution
```cpp
#include <iostream>
#include <string>

int main() {
    std::string s;
    std::cin >> s;
    int count = 0;
    for (char c : s) {
        char lower_c = tolower(c);
        if (lower_c == 'a' || lower_c == 'e' || lower_c == 'i' || lower_c == 'o' || lower_c == 'u') {
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
count = 0
vowels = "aeiou"
for char in s.lower():
    if char in vowels:
        count += 1
print(count)
```
