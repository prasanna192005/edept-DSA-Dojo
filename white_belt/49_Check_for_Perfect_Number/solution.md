# Solution for Problem 49: Check for Perfect Number

## Explanation
The proper divisors of 6 are 1, 2, and 3. Their sum is 1+2+3=6. Find all proper divisors of N, sum them up, and check if the sum equals N.

---

### C++ Solution
```cpp
#include <iostream>

int main() {
    int n;
    std::cin >> n;
    if (n <= 1) {
        std::cout << "No" << std::endl;
        return 0;
    }
    int sum_of_divisors = 1;
    for (int i = 2; i * i <= n; ++i) {
        if (n % i == 0) {
            sum_of_divisors += i;
            if (i * i != n) {
                sum_of_divisors += n / i;
            }
        }
    }
    if (sum_of_divisors == n) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "No" << std::endl;
    }
    return 0;
}
```

### Python Solution
```python
n = int(input())
if n <= 1:
    print("No")
else:
    sum_of_divisors = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum_of_divisors += i
            if i * i != n:
                sum_of_divisors += n // i
    if sum_of_divisors == n:
        print("Yes")
    else:
        print("No")
```
