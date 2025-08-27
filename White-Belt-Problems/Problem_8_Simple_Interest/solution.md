# Solutions for Problem 8: Simple Interest

## C Solution
```c
#include <stdio.h>

int main() {
    int p, t;
    float r;
    scanf("%d %f %d", &p, &r, &t);
    float si = (p * r * t) / 100.0;
    printf("%.1f\n", si);
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>
#include <iomanip>

int main() {
    int p, t;
    double r;
    std::cin >> p >> r >> t;
    double si = (p * r * t) / 100.0;
    std::cout << std::fixed << std::setprecision(1) << si << std::endl;
    return 0;
}
```

## Java Solution
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int p = sc.nextInt();
        float r = sc.nextFloat();
        int t = sc.nextInt();
        float si = (p * r * t) / 100;
        System.out.printf("%.1f\n", si);
    }
}
```

## Python Solution
```python
p, r, t = map(float, input().split())
si = (p * r * t) / 100
print(f"{si:.1f}")
```

## JavaScript Solution
```javascript
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const [p, r, t] = line.split(' ').map(Number);
    const si = (p * r * t) / 100;
    console.log(si.toFixed(1));
    rl.close();
});
```
