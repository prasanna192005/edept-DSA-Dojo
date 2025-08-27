# Solutions for Problem 2: Sum of Two

## C Solution
```c
#include <stdio.h>

int main() {
    long long a, b;
    scanf("%lld %lld", &a, &b);
    printf("%lld\n", a + b);
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>

int main() {
    long long a, b;
    std::cin >> a >> b;
    std::cout << a + b << std::endl;
    return 0;
}
```

## Java Solution
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        long b = sc.nextLong();
        System.out.println(a + b);
    }
}
```

## Python Solution
```python
a, b = map(int, input().split())
print(a + b)
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
    console.log(a + b);
    rl.close();
});
```
