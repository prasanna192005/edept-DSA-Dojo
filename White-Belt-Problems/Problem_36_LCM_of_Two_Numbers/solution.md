# Solutions for Problem 36: LCM of Two Numbers

## C Solution
```c
#include <stdio.h>

long long gcd(long long a, long long b) {
    while (b != 0) {
        long long temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    long long a, b;
    scanf("%lld %lld", &a, &b);
    long long lcm = (a / gcd(a, b)) * b;
    printf("%lld\n", lcm);
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>
#include <algorithm>

int main() {
    long long a, b;
    std::cin >> a >> b;
    long long lcm = (a / std::gcd(a, b)) * b;
    std::cout << lcm << std::endl;
    return 0;
}
```

## Java Solution
```java
import java.util.Scanner;

public class Main {
    public static long gcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        long b = sc.nextLong();
        long lcm = (a / gcd(a, b)) * b;
        System.out.println(lcm);
    }
}
```

## Python Solution
```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
lcm = (a // gcd(a, b)) * b
print(lcm)
```

## JavaScript Solution
```javascript
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const [a, b] = line.split(' ').map(Number);
    const gcd = (a, b) => {
        while (b) {
            [a, b] = [b, a % b];
        }
        return a;
    };
    const lcm = (a / gcd(a, b)) * b;
    console.log(lcm);
    rl.close();
});
```
