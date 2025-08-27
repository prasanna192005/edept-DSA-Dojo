# Solution for Problem 48: Check for Armstrong Number

## Explanation
First, count the number of digits. Then, iterate through the digits of the number again, summing up each digit raised to the power of the total digit count. Compare this sum with the original number.

---

### C++ Solution
```cpp
#include <iostream>
#include <string>
#include <cmath>

int main() {
    int n;
    std::cin >> n;
    std::string s = std::to_string(n);
    int num_digits = s.length();
    int sum = 0;
    int temp = n;
    while (temp > 0) {
        int digit = temp % 10;
        sum += pow(digit, num_digits);
        temp /= 10;
    }
    if (sum == n) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "No" << std::endl;
    }
    return 0;
}
```

### Python Solution
```python
n_str = input()
n = int(n_str)
num_digits = len(n_str)
digit_sum = 0
for digit in n_str:
    digit_sum += int(digit) ** num_digits
if digit_sum == n:
    print("Yes")
else:
    print("No")
```
