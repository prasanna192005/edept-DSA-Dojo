# Solution for Problem 22: Find Maximum in Array

## Explanation
Initialize a `max_val` variable to the first element of the array. Loop through the rest of the array, and if an element is greater than `max_val`, update `max_val`.

---

### C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> arr(n);
    int max_val = -2e9; // A very small number
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
        if (arr[i] > max_val) {
            max_val = arr[i];
        }
    }
    std::cout << max_val << std::endl;
    return 0;
}
```

### Python Solution
```python
n = int(input())
arr = list(map(int, input().split()))
print(max(arr))
```
