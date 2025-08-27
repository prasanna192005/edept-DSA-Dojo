# Solutions for Problem 39: Power of Number

## C Solution
```c
#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    long long result = 1;
    for (int i = 0; i < b; i++) {
        result *= a;
    }
    printf("%lld\n", result);
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>

int main() {
    int a, b;
    std::cin >> a >> b;
    long long result = 1;
    for (int i = 0; i < b; ++i) {
        result *= a;
    }
    std::cout << result << std::endl;
    return 0;
}
```

## Java Solution
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        long result = 1;
        for (int i = 0; i < b; i++) {
            result *= a;
        }
        System.out.println(result);
    }
}
```

## Python Solution
```python
a, b = map(int, input().split())
print(a ** b)
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
    console.log(Math.pow(a, b));
    rl.close();
});
```
