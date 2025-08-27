# Solutions for Problem 16: Reverse Number

## C Solution
```c
#include <stdio.h>

int main() {
    long long n, reversed = 0;
    scanf("%lld", &n);
    int is_negative = n < 0;
    if (is_negative) n = -n;
    while (n > 0) {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }
    printf("%lld\n", is_negative ? -reversed : reversed);
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>

int main() {
    long long n, reversed = 0;
    std::cin >> n;
    int is_negative = n < 0;
    if (is_negative) n = -n;
    while (n > 0) {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }
    std::cout << (is_negative ? -reversed : reversed) << std::endl;
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
        boolean isNegative = n < 0;
        if (isNegative) n = -n;
        long reversed = 0;
        while (n > 0) {
            reversed = reversed * 10 + n % 10;
            n /= 10;
        }
        System.out.println(isNegative ? -reversed : reversed);
    }
}
```

## Python Solution
```python
n = int(input())
is_negative = n < 0
if is_negative:
    n = -n
reversed_num = int(str(n)[::-1])
print(-reversed_num if is_negative else reversed_num)
```

## JavaScript Solution
```javascript
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    let n = parseInt(line);
    const isNegative = n < 0;
    if (isNegative) n = -n;
    const reversed = parseInt(n.toString().split('').reverse().join(''));
    console.log(isNegative ? -reversed : reversed);
    rl.close();
});
```
