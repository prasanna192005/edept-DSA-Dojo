# Solutions for Problem 4: Even or Odd

## C Solution
```c
#include <stdio.h>

int main() {
    long long n;
    scanf("%lld", &n);
    if (n % 2 == 0) {
        printf("Even\n");
    } else {
        printf("Odd\n");
    }
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>

int main() {
    long long n;
    std::cin >> n;
    if (n % 2 == 0) {
        std::cout << "Even" << std::endl;
    } else {
        std::cout << "Odd" << std::endl;
    }
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
        System.out.println(n % 2 == 0 ? "Even" : "Odd");
    }
}
```

## Python Solution
```python
n = int(input())
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
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
    console.log(n % 2 === 0 ? "Even" : "Odd");
    rl.close();
});
```
