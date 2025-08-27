# Solutions for Problem 32: Is Substring

## C Solution
```c
#include <stdio.h>
#include <string.h>

int main() {
    char s[1001], t[1001];
    scanf("%s\n%s", s, t);
    if (strstr(s, t) != NULL) {
        printf("Yes\n");
    } else {
        printf("No\n");
    }
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>
#include <string>

int main() {
    std::string s, t;
    std::cin >> s >> t;
    if (s.find(t) != std::string::npos) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "No" << std::endl;
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
        String s = sc.nextLine();
        String t = sc.nextLine();
        System.out.println(s.contains(t) ? "Yes" : "No");
    }
}
```

## Python Solution
```python
s = input()
t = input()
print("Yes" if t in s else "No")
```

## JavaScript Solution
```javascript
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let input = [];
rl.on('line', (line) => {
    input.push(line);
    if (input.length === 2) {
        const [s, t] = input;
        console.log(s.includes(t) ? "Yes" : "No");
        rl.close();
    }
});
```
