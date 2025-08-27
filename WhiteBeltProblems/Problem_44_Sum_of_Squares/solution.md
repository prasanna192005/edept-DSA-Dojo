# Solutions for Problem 44: Sum of Squares

## C Solution
```c
#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    long long sum = (long long)n * (n + 1) * (2 * n + 1) / 6;
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
    long long sum = (long long)n * (n + 1) * (2 * n + 1) / 6;
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
        long sum = (long)n * (n + 1) * (2 * n + 1) / 6;
        System.out.println(sum);
    }
}
```

## Python Solution
```python
n = int(input())
print(n * (n + 1) * (2 * n + 1) // 6)
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
    const sum = n * (n + 1) * (2 * n + 1) / 6;
    console.log(sum);
    rl.close();
});
```
