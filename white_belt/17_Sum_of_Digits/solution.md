# Solution for Problem 17: Sum of Digits

## Explanation
Use a loop. In each step, get the last digit using modulo 10 and add it to a running sum. Then remove the last digit by dividing by 10.

---

### C++ Solution
```cpp
#include <iostream>

int main() {
    int n;
    std::cin >> n;
    int sum = 0;
    if (n < 0) n = -n; // Make number positive
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    std::cout << sum << std::endl;
    return 0;
}
```

### Python Solution
```python
n_str = input()
if n_str.startswith('-'):
    n_str = n_str[1:]
digit_sum = 0
for digit in n_str:
    digit_sum += int(digit)
print(digit_sum)
```
