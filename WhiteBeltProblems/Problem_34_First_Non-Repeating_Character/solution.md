# Solutions for Problem 34: First Non-Repeating Character

## C Solution
```c
#include <stdio.h>
#include <string.h>

int main() {
    char s[1001];
    scanf("%s", s);
    int freq[26] = {0};
    for (int i = 0; s[i] != '\0'; i++) {
        freq[s[i] - 'a']++;
    }
    for (int i = 0; s[i] != '\0'; i++) {
        if (freq[s[i] - 'a'] == 1) {
            printf("%c\n", s[i]);
            return 0;
        }
    }
    printf("None\n");
    return 0;
}
```

## C++ Solution
```cpp
#include <iostream>
#include <string>
#include <unordered_map>

int main() {
    std::string s;
    std::cin >> s;
    std::unordered_map<char, int> freq;
    for (char c : s) freq[c]++;
    for (char c : s) {
        if (freq[c] == 1) {
            std::cout << c << std::endl;
            return 0;
        }
    }
    std::cout << "None" << std::endl;
    return 0;
}
```

## Java Solution
```java
import java.util.Scanner;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        HashMap<Character, Integer> freq = new HashMap<>();
        for (char c : s.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }
        for (char c : s.toCharArray()) {
            if (freq.get(c) == 1) {
                System.out.println(c);
                return;
            }
        }
        System.out.println("None");
    }
}
```

## Python Solution
```python
s = input()
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
for c in s:
    if freq[c] == 1:
        print(c)
        exit()
print("None")
```

## JavaScript Solution
```javascript
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const freq = {};
    for (let c of line) {
        freq[c] = (freq[c] || 0) + 1;
    }
    for (let c of line) {
        if (freq[c] === 1) {
            console.log(c);
            rl.close();
            return;
        }
    }
    console.log("None");
    rl.close();
});
```
