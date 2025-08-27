# Solution for Problem 25: Count Occurrences

## Explanation
Initialize a counter to 0. Loop through the array. For each element, if it equals the target `X`, increment the counter.

---

### C++ Solution
```cpp
#include <iostream>
#include <vector>

int main() {
    int n, x;
    std::cin >> n >> x;
    std::vector<int> arr(n);
    int count = 0;
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
        if (arr[i] == x) {
            count++;
        }
    }
    std::cout << count << std::endl;
    return 0;
}
```

### Python Solution
```python
n, x = map(int, input().split())
arr = list(map(int, input().split()))
print(arr.count(x))
```
