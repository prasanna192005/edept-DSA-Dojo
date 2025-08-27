# Solutions for Problem 24: Count Positive Numbers

## C Solution
```c
#include <stdio.h>

int main() {
    int n, count = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int x;
        scanf("%d", &x);
        if (x > 0) count++;
    }
    printf("%d\n", count);
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>

int main() {
    int n, count = 0;
    std::cin >> n;
    for (int i = 0; i < n; ++i) {
        int x;
        std::cin >> x;
        if (x > 0) count++;
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
        int n = sc.nextInt();
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (sc.nextInt() > 0) count++;
        }
        System.out.println(count);
    }
}
```

## Python Solution
```python
n = int(input())
arr = list(map(int, input().split()))
print(sum(1 for x in arr if x > 0))
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
        const count = arr.filter(x => x > 0).length;
        console.log(count);
        rl.close();
    }
});
```
