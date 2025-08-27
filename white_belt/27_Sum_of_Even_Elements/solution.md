# Solution for Problem 27: Sum of Even Elements

## Explanation
Initialize a sum to 0. Loop through the array. For each element, check if it's even (`element % 2 == 0`). If it is, add it to the sum.

---

### C++ Solution
```cpp
#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    long long even_sum = 0;
    for (int i = 0; i < n; ++i) {
        int val;
        std::cin >> val;
        if (val % 2 == 0) {
            even_sum += val;
        }
    }
    std::cout << even_sum << std::endl;
    return 0;
}
```

### Python Solution
```python
n = int(input())
arr = list(map(int, input().split()))
even_sum = 0
for num in arr:
    if num % 2 == 0:
        even_sum += num
print(even_sum)
```
