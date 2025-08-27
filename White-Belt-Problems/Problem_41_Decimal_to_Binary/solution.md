# Solutions for Problem 41: Decimal to Binary

## C Solution
```c
#include <stdio.h>
#include <string.h>

int main() {
    long long n;
    scanf("%lld", &n);
    if (n == 0) {
        printf("0\n");
        return 0;
    }
    char binary[33] = {0};
    int i = 0;
    while (n > 0) {
        binary[i++] = (n % 2) + '0';
        n /= 2;
    }
    for (int j = i - 1; j >= 0; j--) {
        printf("%c", binary[j]);
    }
    printf("\n");
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>
#include <string>

int main() {
    long long n;
    std::cin >> n;
    if (n == 0) {
        std::cout << "0" << std::endl;
        return 0;
    }
    std::string binary;
    while (n > 0) {
        binary += (n % 2) + '0';
        n /= 2;
    }
    for (int i = binary.length() - 1; i >= 0; --i) {
        std::cout << binary[i];
    }
    std::cout << std::endl;
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
        if (n == 0) {
            System.out.println("0");
            return;
        }
        StringBuilder binary = new StringBuilder();
        while (n > 0) {
            binary.append(n % 2);
            n /= 2;
        }
        System.out.println(binary.reverse());
    }
}
```

## Python Solution
```python
n = int(input())
if n == 0:
    print("0")
else:
    binary = ""
    while n > 0:
        binary += str(n % 2)
        n //= 2
    print(binary[::-1])
```

## JavaScript Solution
```javascript
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    let n = parseInt(line);
    if (n === 0) {
        console.log("0");
        rl.close();
        return;
    }
    let binary = "";
    while (n > 0) {
        binary += n % 2;
        n = Math.floor(n / 2);
    }
    console.log(binary.split('').reverse().join(''));
    rl.close();
});
```
