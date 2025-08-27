# Solutions for Problem 3: Area of a Rectangle

## C Solution
```c
#include <stdio.h>

int main() {
    int length, width;
    scanf("%d %d", &length, &width);
    printf("%lld\n", (long long)length * width);
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>

int main() {
    int length, width;
    std::cin >> length >> width;
    long long area = (long long)length * width;
    std::cout << area << std::endl;
    return 0;
}
```

## Java Solution
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int length = sc.nextInt();
        int width = sc.nextInt();
        System.out.println((long)length * width);
    }
}
```

## Python Solution
```python
length, width = map(int, input().split())
print(length * width)
```

## JavaScript Solution
```javascript
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const [length, width] = line.split(' ').map(Number);
    console.log(length * width);
    rl.close();
});
```
