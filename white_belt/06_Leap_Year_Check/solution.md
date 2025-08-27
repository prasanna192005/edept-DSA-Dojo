# Solution for Problem 06: Leap Year Check

## Explanation
A year is a leap year if `(year % 4 == 0 AND year % 100 != 0) OR (year % 400 == 0)`.

---

### C++ Solution
```cpp
#include <iostream>

int main() {
    int year;
    std::cin >> year;
    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "No" << std::endl;
    }
    return 0;
}
```

### Python Solution
```python
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Yes")
else:
    print("No")
```
