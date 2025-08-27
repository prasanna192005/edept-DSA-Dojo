# Solutions for Problem 18: Print Even Numbers

## C Solution
```c
#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 2; i <= n; i += 2) {
        printf("%d", i);
        if (i < n) printf(" ");
    }
    printf("\n");
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>

int main() {
    int n;
    std::cin >> n;
    for (int i = 2; i <= n; i += 2) {
        std::cout << i;
        if (i < n) std::cout << " ";
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
        int n = sc.nextInt();
        for (int i = 2; i <= n; i += 2) {
            System.out.print(i);
            if (i < n) System.out.print(" ");
        }
        System.out.println();
    }
}
```

## Python Solution
```python
n = int(input())
print(*[i for i in range(2, n + 1, 2)])
```

## JavaScript Solution
```javascript
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const n = parseInt(line);
    const evens = [];
    for (let i = 2; i <= n; i += 2) {
        evens.push(i);
    }
    console.log(evens.join(' '));
    rl.close();
});
```
