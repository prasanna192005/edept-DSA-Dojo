# Solutions for Problem 40: Binary to Decimal

## C Solution
```c
#include <stdio.h>
#include <string.h>

int main() {
    char s[33];
    scanf("%s", s);
    long long decimal = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        decimal = decimal * 2 + (s[i] - '0');
    }
    printf("%lld\n", decimal);
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>
#include <string>

int main() {
    std::string s;
    std::cin >> s;
    long long decimal = 0;
    for (char c : s) {
        decimal = decimal * 2 + (c - '0');
    }
    std::cout << decimal << std::endl;
    return 0;
}
```

## Java Solution
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        long decimal = 0;
        for (char c : s.toCharArray()) {
            decimal = decimal * 2 + (c - '0');
        }
        System.out.println(decimal);
    }
}
```

## Python Solution
```python
s = input()
print(int(s, 2))
```

## JavaScript Solution
```javascript
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    console.log(parseInt(line, 2));
    rl.close();
});
```
