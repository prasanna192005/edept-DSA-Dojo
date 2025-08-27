# Solution for Problem 15: Count Digits

## Explanation
Use a while loop. Repeatedly divide the number by 10 and increment a counter until the number becomes 0. A special case is input 0, which has 1 digit.

---

### C++ Solution
```cpp
#include <iostream>

int main() {
    int n;
    std::cin >> n;
    if (n == 0) {
        std::cout << 1 << std::endl;
        return 0;
    }
    int count = 0;
    long long temp_n = n; // Use long long to handle absolute of INT_MIN
    if (temp_n < 0) temp_n = -temp_n;
    while (temp_n > 0) {
        temp_n /= 10;
        count++;
    }
    std::cout << count << std::endl;
    return 0;
}
```

### Python Solution
```python
n_str = input()
if n_str.startswith('-'):
    print(len(n_str) - 1)
else:
    print(len(n_str))
```
