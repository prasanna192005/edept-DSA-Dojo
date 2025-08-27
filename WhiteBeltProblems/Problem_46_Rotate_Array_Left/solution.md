# Solutions for Problem 46: Rotate Array Left

## C Solution
```c
#include <stdio.h>

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    int arr[1000];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    k = k % n;
    for (int i = 0; i < n; i++) {
        printf("%d", arr[(i + k) % n]);
        if (i < n - 1) printf(" ");
    }
    printf("\n");
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>
#include <vector>

int main() {
    int n, k;
    std::cin >> n >> k;
    std::vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }
    k = k % n;
    for (int i = 0; i < n; ++i) {
        std::cout << arr[(i + k) % n];
        if (i < n - 1) std::cout << " ";
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
        int k = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        k = k % n;
        for (int i = 0; i < n; i++) {
            System.out.print(arr[(i + k) % n]);
            if (i < n - 1) System.out.print(" ");
        }
        System.out.println();
    }
}
```

## Python Solution
```python
n, k = map(int, input().split())
arr = list(map(int, input().split()))
k = k % n
print(*(arr[(i + k) % n] for i in range(n)))
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
        const [n, k] = input[0].split(' ').map(Number);
        const arr = input[1].split(' ').map(Number);
        const rotated = [];
        for (let i = 0; i < n; i++) {
            rotated.push(arr[(i + k) % n]);
        }
        console.log(rotated.join(' '));
        rl.close();
    }
});
```
