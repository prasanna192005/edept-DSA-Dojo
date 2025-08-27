# Solutions for Problem 38: Sum of Primes

## C Solution
```c
#include <stdio.h>
#include <math.h>

int is_prime(int n) {
    if (n < 2) return 0;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int main() {
    int n;
    scanf("%d", &n);
    long long sum = 0;
    for (int i = 2; i <= n; i++) {
        if (is_prime(i)) sum += i;
    }
    printf("%lld\n", sum);
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>
#include <cmath>

bool is_prime(int n) {
    if (n < 2) return false;
    for (int i = 2; i <= std::sqrt(n); ++i) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    int n;
    std::cin >> n;
    long long sum = 0;
    for (int i = 2; i <= n; ++i) {
        if (is_prime(i)) sum += i;
    }
    std::cout << sum << std::endl;
    return 0;
}
```

## Java Solution
```java
import java.util.Scanner;

public class Main {
    public static boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long sum = 0;
        for (int i = 2; i <= n; i++) {
            if (isPrime(i)) sum += i;
        }
        System.out.println(sum);
    }
}
```

## Python Solution
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
print(sum(i for i in range(2, n + 1) if is_prime(i)))
```

## JavaScript Solution
```javascript
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const n = parseInt(line);
    const isPrime = (n) => {
        if (n < 2) return false;
        for (let i = 2; i <= Math.sqrt(n); i++) {
            if (n % i === 0) return false;
        }
        return true;
    };
    let sum = 0;
    for (let i = 2; i <= n; i++) {
        if (isPrime(i)) sum += i;
    }
    console.log(sum);
    rl.close();
});
```
