# Solutions for Problem 7: Largest of Three Numbers

## C Solution
```c
#include <stdio.h>

int main() {
    long long a, b, c;
    scanf("%lld %lld %lld", &a, &b, &c);
    long long max = a;
    if (b > max) max = b;
    if (c > max) max = c;
    printf("%lld\n", max);
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>
#include <algorithm>

int main() {
    long long a, b, c;
    std::cin >> a >> b >> c;
    std::cout << std::max({a, b, c}) << std::endl;
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
        long c = sc.nextLong();
        System.out.println(Math.max(a, Math.max(b, c)));
    }
}
```

## Python Solution
```python
a, b, c = map(int, input().split())
print(max(a, b, c))
```

## JavaScript Solution
```javascript
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const [a, b, c] = line.split(' ').map(Number);
    console.log(Math.max(a, b, c));
    rl.close();
});
```
