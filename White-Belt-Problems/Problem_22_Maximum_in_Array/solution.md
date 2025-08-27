# Solutions for Problem 22: Maximum in Array

## C Solution
```c
#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int max = -1000001;
    for (int i = 0; i < n; i++) {
        int x;
        scanf("%d", &x);
        if (x > max) max = x;
    }
    printf("%d\n", max);
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;
    int max = -1000001;
    for (int i = 0; i < n; ++i) {
        int x;
        std::cin >> x;
        max = std::max(max, x);
    }
    std::cout << max << std::endl;
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
        int max = -1000001;
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            max = Math.max(max, x);
        }
        System.out.println(max);
    }
}
```

## Python Solution
```python
n = int(input())
arr = list(map(int, input().split()))
print(max(arr))
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
        const arr = input[1].split(' ').map(Number);
        console.log(Math.max(...arr));
        rl.close();
    }
});
```
