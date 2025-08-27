# Solutions for Problem 30: Uppercase to Lowercase

## C Solution
```c
#include <stdio.h>
#include <string.h>

int main() {
    char s[1001];
    scanf("%s", s);
    for (int i = 0; s[i] != '\0'; i++) {
        s[i] = s[i] + 32;
    }
    printf("%s\n", s);
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>
#include <string>
#include <algorithm>

int main() {
    std::string s;
    std::cin >> s;
    for (char &c : s) {
        c = c + 32;
    }
    std::cout << s << std::endl;
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
        StringBuilder result = new StringBuilder();
        for (char c : s.toCharArray()) {
            result.append((char)(c + 32));
        }
        System.out.println(result);
    }
}
```

## Python Solution
```python
s = input()
print(s.lower())
```

## JavaScript Solution
```javascript
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    console.log(line.toLowerCase());
    rl.close();
});
```
