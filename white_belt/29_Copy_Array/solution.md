# Solution for Problem 29: Copy Array

## Explanation
Declare a new array of the same size. Loop through the original array and assign each element to the corresponding position in the new array.

---

### C++ Solution
```cpp
#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> original(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> original[i];
    }
    std::vector<int> copied = original;
    for (int i = 0; i < n; ++i) {
        std::cout << copied[i] << (i == n - 1 ? "" : " ");
    }
    std::cout << std::endl;
    return 0;
}
```

### Python Solution
```python
n = int(input())
original = list(map(int, input().split()))
copied = list(original) # or original[:]
print(*copied)
```
