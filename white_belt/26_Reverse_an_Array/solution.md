# Solution for Problem 26: Reverse an Array

## Explanation
One way is to create a new array and populate it by iterating the original array backward. Another is to swap elements in-place using two pointers, one at the start and one at the end, moving towards the center.

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
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }
    std::reverse(arr.begin(), arr.end());
    for (int i = 0; i < n; ++i) {
        std::cout << arr[i] << (i == n - 1 ? "" : " ");
    }
    std::cout << std::endl;
    return 0;
}
```

### Python Solution
```python
n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
print(*arr)
```
