# Solutions for Problem 42: Square Root Integer

## C Solution
```c
#include <stdio.h>
#include <math.h>

int main() {
    long long n;
    scanf("%lld", &n);
    printf("%lld\n", (long long)sqrt(n));
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>
#include <cmath>

int main() {
    long long n;
    std::cin >> n;
    std::cout << (long long)std::sqrt(n) << std::endl;
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
        System.out.println((long)Math.sqrt(n));
    }
}
```

## Python Solution
```python
n = int(input())
print(int(n ** 0.5))
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
    console.log(Math.floor(Math.sqrt(n)));
    rl.close();
});
```
