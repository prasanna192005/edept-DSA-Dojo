# Solutions for Problem 9: Temperature Conversion

## C Solution
```c
#include <stdio.h>

int main() {
    float celsius;
    scanf("%f", &celsius);
    float fahrenheit = celsius * 9.0 / 5.0 + 32;
    printf("%.1f\n", fahrenheit);
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>
#include <iomanip>

int main() {
    double celsius;
    std::cin >> celsius;
    double fahrenheit = celsius * 9.0 / 5.0 + 32;
    std::cout << std::fixed << std::setprecision(1) << fahrenheit << std::endl;
    return 0;
}
```

## Java Solution
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double celsius = sc.nextDouble();
        double fahrenheit = celsius * 9.0 / 5.0 + 32;
        System.out.printf("%.1f\n", fahrenheit);
    }
}
```

## Python Solution
```python
celsius = float(input())
fahrenheit = celsius * 9/5 + 32
print(f"{fahrenheit:.1f}")
```

## JavaScript Solution
```javascript
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const celsius = parseFloat(line);
    const fahrenheit = celsius * 9/5 + 32;
    console.log(fahrenheit.toFixed(1));
    rl.close();
});
```
