# Solutions for Problem 33: Toggle Case

## C Solution
```c
#include <stdio.h>
#include <string.h>

int main() {
    char s[1001];
    scanf("%s", s);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] >= 'A' && s[i] <= 'Z') {
            s[i] += 32;
        } else if (s[i] >= 'a' && s[i] <= 'z') {
            s[i] -= 32;
        }
    }
    printf("%s\n", s);
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
    for (char &c : s) {
        if (c >= 'A' && c <= 'Z') c += 32;
        else if (c >= 'a' && c <= 'z') c -= 32;
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
            if (Character.isUpperCase(c)) {
                result.append(Character.toLowerCase(c));
            } else {
                result.append(Character.toUpperCase(c));
            }
        }
        System.out.println(result);
    }
}
```

## Python Solution
```python
s = input()
print(''.join(c.lower() if c.isupper() else c.upper() for c in s))
```

## JavaScript Solution
```javascript
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const result = line.split('').map(c => 
        c === c.toUpperCase() ? c.toLowerCase() : c.toUpperCase()
    ).join('');
    console.log(result);
    rl.close();
});
```
