# Solutions for Problem 14: Factorial Iterative

## C Solution
```c
#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    long long factorial = 1;
    for (int i = 1; i <= n; i++) {
        factorial *= i;
    }
    printf("%lld\n", factorial);
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>

int main() {
    int n;
    std::cin >> n;
    long long factorial = 1;
    for (int i = 1; i <= n; ++i) {
        factorial *= i;
    }
    std::cout << factorial << std::endl;
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
        long factorial = 1;
        for (int i = 1; i <= n; i++) {
            factorial *= i;
        }
        System.out.println(factorial);
    }
}
```

## Python Solution
```python
n = int(input())
factorial = 1
if n == 0:
    print(1)
else:
    for i in range(1, n + 1):
        factorial *= i
    print(factorial)
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
    let factorial = 1n;
    for (let i = 1; i <= n; i++) {
        factorial *= BigInt(i);
    }
    console.log(factorial.toString());
    rl.close();
});
```
