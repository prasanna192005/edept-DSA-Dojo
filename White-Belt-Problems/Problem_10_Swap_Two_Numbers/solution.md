# Solutions for Problem 10: Swap Two Numbers

## C Solution
```c
#include <stdio.h>

int main() {
    long long a, b, temp;
    scanf("%lld %lld", &a, &b);
    temp = a;
    a = b;
    b = temp;
    printf("%lld %lld\n", a, b);
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>

int main() {
    long long a, b;
    std::cin >> a >> b;
    std::swap(a, b);
    std::cout << a << " " << b << std::endl;
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
        long temp = a;
        a = b;
        b = temp;
        System.out.println(a + " " + b);
    }
}
```

## Python Solution
```python
a, b = map(int, input().split())
a, b = b, a
print(a, b)
```

## JavaScript Solution
```javascript
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    let [a, b] = line.split(' ').map(Number);
    [a, b] = [b, a];
    console.log(a + " " + b);
    rl.close();
});
```
