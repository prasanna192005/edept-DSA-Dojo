# Solutions for Problem 31: Count Characters

## C Solution
```c
#include <stdio.h>
#include <string.h>

int main() {
    char s[1001], c;
    scanf("%s\n%c", s, &c);
    int count = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == c) count++;
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
    char c;
    std::cin >> s >> c;
    int count = 0;
    for (char x : s) {
        if (x == c) count++;
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
        String s = sc.nextLine();
        char c = sc.nextLine().charAt(0);
        int count = 0;
        for (char x : s.toCharArray()) {
            if (x == c) count++;
        }
        System.out.println(count);
    }
}
```

## Python Solution
```python
s = input()
c = input()
print(s.count(c))
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
        const s = input[0];
        const c = input[1];
        let count = 0;
        for (let x of s) {
            if (x === c) count++;
        }
        console.log(count);
        rl.close();
    }
});
```
