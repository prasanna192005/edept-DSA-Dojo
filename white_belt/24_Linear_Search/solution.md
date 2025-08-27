# Solution for Problem 24: Linear Search

## Explanation
Iterate through the array from the beginning. For each element, check if it equals the target `X`. If it does, print the current index and stop. If the loop finishes without finding `X`, print -1.

---

### C++ Solution
```cpp
#include <iostream>
#include <vector>

int main() {
    int n, x;
    std::cin >> n >> x;
    std::vector<int> arr(n);
    int found_index = -1;
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
        if (arr[i] == x && found_index == -1) {
            found_index = i;
        }
    }
    std::cout << found_index << std::endl;
    return 0;
}
```

### Python Solution
```python
n, x = map(int, input().split())
arr = list(map(int, input().split()))
try:
    print(arr.index(x))
except ValueError:
    print(-1)
```
