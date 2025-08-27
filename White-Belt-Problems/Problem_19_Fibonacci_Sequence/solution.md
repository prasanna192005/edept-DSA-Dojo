# Solutions for Problem 19: Fibonacci Sequence

## C Solution
```c
#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    long long a = 0, b = 1;
    if (n >= 1) printf("%lld", a);
    if (n >= 2) printf(" %lld", b);
    for (int i = 3; i <= n; i++) {
        long long next = a + b;
        printf(" %lld", next);
        a = b;
        b = next;
    }
    printf("\n");
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>

int main() {
    int n;
    std::cin >> n;
    long long a = 0, b = 1;
    if (n >= 1) std::cout << a;
    if (n >= 2) std::cout << " " << b;
    for (int i = 3; i <= n; ++i) {
        long long next = a + b;
        std::cout << " " << next;
        a = b;
        b = next;
    }
    std::cout << std::endl;
    return 0;
}
```

## Java Solution
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long a = 0, b = 1;
        if (n >= 1) System.out.print(a);
        if (n >= 2) System.out.print(" " + b);
        for (int i = 3; i <= n; i++) {
            long next = a + b;
            System.out.print(" " + next);
            a = b;
            b = next;
        }
        System.out.println();
    }
}
```

## Python Solution
```python
n = int(input())
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
print(*fib[:n])
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
    const fib = [0, 1];
    for (let i = 2; i < n; i++) {
        fib.push(fib[i-1] + fib[i-2]);
    }
    console.log(fib.slice(0, n).join(' '));
    rl.close();
});
```
