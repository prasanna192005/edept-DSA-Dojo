# Solutions for Problem 37: Prime Number Check

## C Solution
```c
#include <stdio.h>
#include <math.h>

int main() {
    long long n;
    scanf("%lld", &n);
    if (n < 2) {
        printf("No\n");
        return 0;
    }
    int is_prime = 1;
    for (long long i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            is_prime = 0;
            break;
        }
    }
    printf("%s\n", is_prime ? "Yes" : "No");
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>
#include <cmath>

int main() {
    long long n;
    std::cin >> n;
    if (n < 2) {
        std::cout << "No" << std::endl;
        return 0;
    }
    bool is_prime = true;
    for (long long i = 2; i <= std::sqrt(n); ++i) {
        if (n % i == 0) {
            is_prime = false;
            break;
        }
    }
    std::cout << (is_prime ? "Yes" : "No") << std::endl;
    return 0;
}
```

## Java Solution
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        if (n < 2) {
            System.out.println("No");
            return;
        }
        boolean isPrime = true;
        for (long i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                isPrime = false;
                break;
            }
        }
        System.out.println(isPrime ? "Yes" : "No");
    }
}
```

## Python Solution
```python
n = int(input())
if n < 2:
    print("No")
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    print("Yes" if is_prime else "No")
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
    if (n < 2) {
        console.log("No");
        rl.close();
        return;
    }
    let isPrime = true;
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            isPrime = false;
            break;
        }
    }
    console.log(isPrime ? "Yes" : "No");
    rl.close();
});
```
