# Solutions for Problem 49: Sum of Odd Numbers

## C Solution
```c
#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    long long sum = 0;
    for (int i = 1; i <= n; i += 2) {
        sum += i;
    }
    printf("%lld\n", sum);
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>

int main() {
    int n;
    std::cin >> n;
    long long sum = 0;
    for (int i = 1; i <= n; i += 2) {
        sum += i;
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
        int n = sc.nextInt();
        long sum = 0;
        for (int i = 1; i <= n; i += 2) {
            sum += i;
        }
        System.out.println(sum);
    }
}
```

## Python Solution
```python
n = int(input())
sum_odds = sum(i for i in range(1, n + 1, 2))
print(sum_odds)
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
    let sum = 0;
    for (let i = 1; i <= n; i += 2) {
        sum += i;
    }
    console.log(sum);
    rl.close();
});
```
