# Solution for Problem 45: Sieve of Eratosthenes Intro

## Explanation
Create a boolean array `is_prime` of size `N+1`, initially all true. Mark 0 and 1 as not prime. Iterate from 2 up to `sqrt(N)`. If a number `p` is prime, mark all its multiples as not prime.

---

### C++ Solution
```cpp
#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<bool> is_prime(n + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int p = 2; p * p <= n; p++) {
        if (is_prime[p]) {
            for (int i = p * p; i <= n; i += p)
                is_prime[i] = false;
        }
    }
    for (int p = 2; p <= n; p++) {
        if (is_prime[p]) {
            std::cout << p << " ";
        }
    }
    std::cout << std::endl;
    return 0;
}
```

### Python Solution
```python
n = int(input())
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False
for p in range(2, int(n**0.5) + 1):
    if is_prime[p]:
        for i in range(p * p, n + 1, p):
            is_prime[i] = False
primes = [p for p in range(n + 1) if is_prime[p]]
print(*primes)
```
