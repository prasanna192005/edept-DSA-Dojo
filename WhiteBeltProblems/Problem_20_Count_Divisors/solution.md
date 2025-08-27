# Solutions for Problem 20: Count Divisors

## C Solution
```c
#include <stdio.h>
#include <math.h>

int main() {
    int n, count = 0;
    scanf("%d", &n);
    for (int i = 1; i <= sqrt(n); i++) {
        if (n % i == 0) {
            count++;
            if (i != n / i) count++;
        }
    }
    printf("%d\n", count);
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>
#include <cmath>

int main() {
    int n, count = 0;
    std::cin >> n;
    for (int i = 1; i <= std::sqrt(n); ++i) {
        if (n % i == 0) {
            count++;
            if (i != n / i) count++;
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
        int n = sc.nextInt();
        int count = 0;
        for (int i = 1; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                count++;
                if (i != n / i) count++;
            }
        }
        System.out.println(count);
    }
}
```

## Python Solution
```python
n = int(input())
count = 0
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        count += 1
        if i != n // i:
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
    const n = parseInt(line);
    let count = 0;
    for (let i = 1; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            count++;
            if (i !== n / i) count++;
        }
    }
    console.log(count);
    rl.close();
});
```
