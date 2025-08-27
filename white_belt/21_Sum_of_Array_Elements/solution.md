# Solution for Problem 21: Sum of Array Elements

## Explanation
Initialize a sum variable to 0. Loop through each element of the array and add it to the sum.

---

### C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <numeric>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> arr(n);
    long long sum = 0;
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
        sum += arr[i];
    }
    std::cout << sum << std::endl;
    return 0;
}
```

### Python Solution
```python
n = int(input())
arr = list(map(int, input().split()))
print(sum(arr))
```
