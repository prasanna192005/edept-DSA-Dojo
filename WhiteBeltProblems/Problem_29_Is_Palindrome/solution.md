# Solutions for Problem 29: Is Palindrome

## C Solution
```c
#include <stdio.h>
#include <string.h>

int main() {
    char s[1001];
    scanf("%s", s);
    int len = strlen(s);
    int is_palindrome = 1;
    for (int i = 0; i < len / 2; i++) {
        if (s[i] != s[len - 1 - i]) {
            is_palindrome = 0;
            break;
        }
    }
    printf("%s\n", is_palindrome ? "Yes" : "No");
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
    int len = s.length();
    bool is_palindrome = true;
    for (int i = 0; i < len / 2; ++i) {
        if (s[i] != s[len - 1 - i]) {
            is_palindrome = false;
            break;
        }
    }
    std::cout << (is_palindrome ? "Yes" : "No") << std::endl;
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
        int len = s.length();
        boolean isPalindrome = true;
        for (int i = 0; i < len / 2; i++) {
            if (s.charAt(i) != s.charAt(len - 1 - i)) {
                isPalindrome = false;
                break;
            }
        }
        System.out.println(isPalindrome ? "Yes" : "No");
    }
}
```

## Python Solution
```python
s = input()
print("Yes" if s == s[::-1] else "No")
```

## JavaScript Solution
```javascript
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const reversed = line.split('').reverse().join('');
    console.log(line === reversed ? "Yes" : "No");
    rl.close();
});
```
