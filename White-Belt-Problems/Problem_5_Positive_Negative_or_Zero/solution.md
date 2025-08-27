# Solutions for Problem 5: Positive Negative or Zero

## C Solution
```c
#include <stdio.h>

int main() {
    long long n;
    scanf("%lld", &n);
    if (n > 0) {
        printf("Positive\n");
    } else if (n < 0) {
        printf("Negative\n");
    } else {
        printf("Zero\n");
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
    if (n > 0) {
        std::cout << "Positive" << std::endl;
    } else if (n < 0) {
        std::cout << "Negative" << std::endl;
    } else {
        std::cout << "Zero" << std::endl;
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
        if (n > 0) {
            System.out.println("Positive");
        } else if (n < 0) {
            System.out.println("Negative");
        } else {
            System.out.println("Zero");
        }
    }
}
```

## Python Solution
```python
n = int(input())
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
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
    if (n > 0) {
        console.log("Positive");
    } else if (n < 0) {
        console.log("Negative");
    } else {
        console.log("Zero");
    }
    rl.close();
});
```
