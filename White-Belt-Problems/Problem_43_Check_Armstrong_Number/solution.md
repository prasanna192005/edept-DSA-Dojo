# Solutions for Problem 43: Check Armstrong Number

## C Solution
```c
#include <stdio.h>
#include <math.h>

int main() {
    long long n;
    scanf("%lld", &n);
    long long temp = n, sum = 0;
    int digits = 0;
    while (temp > 0) {
        digits++;
        temp /= 10;
    }
    temp = n;
    while (temp > 0) {
        sum += pow(temp % 10, digits);
        temp /= 10;
    }
    printf("%s\n", sum == n ? "Yes" : "No");
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
    long long temp = n, sum = 0;
    int digits = 0;
    while (temp > 0) {
        digits++;
        temp /= 10;
    }
    temp = n;
    while (temp > 0) {
        sum += std::pow(temp % 10, digits);
        temp /= 10;
    }
    std::cout << (sum == n ? "Yes" : "No") << std::endl;
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
        long temp = n, sum = 0;
        int digits = 0;
        while (temp > 0) {
            digits++;
            temp /= 10;
        }
        temp = n;
        while (temp > 0) {
            sum += Math.pow(temp % 10, digits);
            temp /= 10;
        }
        System.out.println(sum == n ? "Yes" : "No");
    }
}
```

## Python Solution
```python
n = int(input())
digits = len(str(n))
sum_powers = sum(int(d) ** digits for d in str(n))
print("Yes" if sum_powers == n else "No")
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
    const digits = n.toString().length;
    const sum = n.toString().split('').reduce((acc, d) => acc + Math.pow(parseInt(d), digits), 0);
    console.log(sum === n ? "Yes" : "No");
    rl.close();
});
```
