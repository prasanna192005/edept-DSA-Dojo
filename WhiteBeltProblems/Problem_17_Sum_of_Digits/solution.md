# Solutions for Problem 17: Sum of Digits

## C Solution
```c
#include <stdio.h>

int main() {
    long long n;
    scanf("%lld", &n);
    if (n < 0) n = -n;
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    printf("%d\n", sum);
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>

int main() {
    long long n;
    std::cin >> n;
    if (n < 0) n = -n;
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    std::cout << sum << std::endl;
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
        if (n < 0) n = -n;
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        System.out.println(sum);
    }
}
```

## Python Solution
```python
n = abs(int(input()))
print(sum(int(digit) for digit in str(n)))
```

## JavaScript Solution
```javascript
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const n = Math.abs(parseInt(line));
    const sum = n.toString().split('').reduce((acc, digit) => acc + parseInt(digit), 0);
    console.log(sum);
    rl.close();
});
```
