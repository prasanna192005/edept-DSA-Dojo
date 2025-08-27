# Solutions for Problem 28: Count Vowels

## C Solution
```c
#include <stdio.h>
#include <string.h>

int main() {
    char s[1001];
    scanf("%s", s);
    int count = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u') {
            count++;
        }
    }
    printf("%d\n", count);
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
    int count = 0;
    for (char c : s) {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            count++;
        }
    }
    std::cout << count << std::endl;
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
        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                count++;
            }
        }
        System.out.println(count);
    }
}
```

## Python Solution
```python
s = input()
print(sum(1 for c in s if c in 'aeiou'))
```

## JavaScript Solution
```javascript
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const vowels = ['a', 'e', 'i', 'o', 'u'];
    const count = line.split('').filter(c => vowels.includes(c)).length;
    console.log(count);
    rl.close();
});
```
