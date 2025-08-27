# Solutions for Problem 47: Factorial Recursive

## C Solution
```c
#include <stdio.h>

long long factorial(int n) {
    if (n == 0) return 1;
    return n * factorial(n - 1);
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%lld\n", factorial(n));
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>

long long factorial(int n) {
    if (n == 0) return 1;
    return n * factorial(n - 1);
}

int main() {
    int n;
    std::cin >> n;
    std::cout << factorial(n) << std::endl;
    return 0;
}
```

## Java Solution
```java
import java.util.Scanner;

public class Main {
    public static long factorial(int n) {
        if (n == 0) return 1;
        return n * factorial(n - 1);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(factorial(n));
    }
}
```

## Python Solution
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

n = int(input())
print(factorial(n))
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
    const factorial = (n) => {
        if (n === 0) return 1n;
        return BigInt(n) * factorial(n - 1);
    };
    console.log(factorial(n).toString());
    rl.close();
});
```
