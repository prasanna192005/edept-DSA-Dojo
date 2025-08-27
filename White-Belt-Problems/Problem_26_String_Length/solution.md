# Solutions for Problem 26: String Length

## C Solution
```c
#include <stdio.h>

int main() {
    char s[1001];
    scanf("%s", s);
    int len = 0;
    while (s[len] != '\0') len++;
    printf("%d\n", len);
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
    int len = 0;
    for (char c : s) len++;
    std::cout << len << std::endl;
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
        int len = 0;
        for (char c : s.toCharArray()) len++;
        System.out.println(len);
    }
}
```

## Python Solution
```python
s = input()
count = 0
for _ in s:
    count += 1
print(count)
```

## JavaScript Solution
```javascript
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    let len = 0;
    for (let c of line) len++;
    console.log(len);
    rl.close();
});
```
