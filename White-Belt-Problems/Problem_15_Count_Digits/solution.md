# Solutions for Problem 15: Count Digits

## C Solution
```c
#include <stdio.h>

int main() {
    long long n;
    scanf("%lld", &n);
    if (n == 0) {
        printf("1\n");
        return 0;
    }
    int count = 0;
    if (n < 0) n = -n;
    while (n > 0) {
        n /= 10;
        count++;
    }
    printf("%d\n", count);
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>

int main() {
    long long n;
    std::cin >> n;
    if (n == 0) {
        std::cout << 1 << std::endl;
        return 0;
    }
    int count = 0;
    if (n < 0) n = -n;
    while (n > 0) {
        n /= 10;
        count++;
    }
    std::cout << count << std::endl;
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
        if (n == 0) {
            System.out.println(1);
            return;
        }
        if (n < 0) n = -n;
        int count = 0;
        while (n > 0) {
            n /= 10;
            count++;
        }
        System.out.println(count);
    }
}
```

## Python Solution
```python
n = int(input())
if n == 0:
    print(1)
else:
    print(len(str(abs(n))))
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
    if (n === 0) {
        console.log(1);
    } else {
        console.log(String(Math.abs(n)).length);
    }
    rl.close();
});
```
