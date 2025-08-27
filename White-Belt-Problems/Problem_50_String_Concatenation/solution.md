# Solutions for Problem 50: String Concatenation

## C Solution
```c
#include <stdio.h>
#include <string.h>

int main() {
    char s[1001], t[1001];
    scanf("%s\n%s", s, t);
    printf("%s%s\n", s, t);
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
    std::cout << s + t << std::endl;
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
        System.out.println(s + t);
    }
}
```

## Python Solution
```python
s = input()
t = input()
print(s + t)
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
        console.log(s + t);
        rl.close();
    }
});
```
