# Solution for Problem 16: Reverse a Number

## Explanation
Use a loop. In each step, get the last digit using modulo 10. Append it to the reversed number and then remove the last digit from the original number by dividing by 10.

---

### C++ Solution
```cpp
#include <iostream>

int main() {
    int n;
    std::cin >> n;
    int reversed_number = 0;
    while (n > 0) {
        int digit = n % 10;
        reversed_number = reversed_number * 10 + digit;
        n /= 10;
    }
    std::cout << reversed_number << std::endl;
    return 0;
}
```

### Python Solution
```python
n_str = input()
print(int(n_str[::-1]))
```
