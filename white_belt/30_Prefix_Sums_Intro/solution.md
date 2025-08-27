# Solution for Problem 30: Prefix Sums Intro

## Explanation
Create a new array `prefix_sum` of size `N`. The first element `prefix_sum[0]` is `arr[0]`. For all other elements `i`, `prefix_sum[i] = prefix_sum[i-1] + arr[i]`.

---

### C++ Solution
```cpp
#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> arr(n);
    std::vector<long long> prefix_sum(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }
    
    prefix_sum[0] = arr[0];
    for (int i = 1; i < n; ++i) {
        prefix_sum[i] = prefix_sum[i-1] + arr[i];
    }

    for (int i = 0; i < n; ++i) {
        std::cout << prefix_sum[i] << (i == n - 1 ? "" : " ");
    }
    std::cout << std::endl;
    return 0;
}
```

### Python Solution
```python
n = int(input())
arr = list(map(int, input().split()))
prefix_sum = [0] * n
prefix_sum[0] = arr[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]
print(*prefix_sum)
```
