# Solutions for Problem 25: Array Element Frequency

## C Solution
```c
#include <stdio.h>

int main() {
    int n, x, count = 0;
    scanf("%d %d", &n, &x);
    for (int i = 0; i < n; i++) {
        int a;
        scanf("%d", &a);
        if (a == x) count++;
    }
    printf("%d\n", count);
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>

int main() {
    int n, x, count = 0;
    std::cin >> n >> x;
    for (int i = 0; i < n; ++i) {
        int a;
        std::cin >> a;
        if (a == x) count++;
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
        int x = sc.nextInt();
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (sc.nextInt() == x) count++;
        }
        System.out.println(count);
    }
}
```

## Python Solution
```python
n, x = map(int, input().split())
arr = list(map(int, input().split()))
print(arr.count(x))
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
        const [n, x] = input[0].split(' ').map(Number);
        const arr = input[1].split(' ').map(Number);
        const count = arr.filter(a => a === x).length;
        console.log(count);
        rl.close();
    }
});
```
