# Solution for Problem 23: Find Minimum in Array

## Explanation
Initialize a `min_val` variable to the first element of the array. Loop through the rest of the array, and if an element is smaller than `min_val`, update `min_val`.

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
    int min_val = 2e9; // A very large number
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
        if (arr[i] < min_val) {
            min_val = arr[i];
        }
    }
    std::cout << min_val << std::endl;
    return 0;
}
```

### Python Solution
```python
n = int(input())
arr = list(map(int, input().split()))
print(min(arr))
```
