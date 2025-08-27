# Solution for Problem 28: Average of Array

## Explanation
First, calculate the sum of all elements in the array. Then, divide the sum by the number of elements (`N`). Use floating-point division.

---

### C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <iomanip>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> arr(n);
    double sum = 0;
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
        sum += arr[i];
    }
    double average = sum / n;
    std::cout << std::fixed << std::setprecision(1) << average << std::endl;
    return 0;
}
```

### Python Solution
```python
n = int(input())
arr = list(map(int, input().split()))
average = sum(arr) / n
print(average)
```
