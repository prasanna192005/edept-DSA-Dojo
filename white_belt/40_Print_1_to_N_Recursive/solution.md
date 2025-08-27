# Solution for Problem 40: Print 1 to N Recursive

## Explanation
Create a function `print_nums(n)`. The base case is when `n < 1`. The recursive step is to call `print_nums(n-1)` first, and then print `n`.

---

### C++ Solution
```cpp
#include <iostream>

void print_nums(int n) {
    if (n < 1) {
        return;
    }
    print_nums(n - 1);
    std::cout << n << std::endl;
}

int main() {
    int n;
    std::cin >> n;
    print_nums(n);
    return 0;
}
```

### Python Solution
```python
def print_nums(n):
    if n < 1:
        return
    print_nums(n - 1)
    print(n)

n = int(input())
print_nums(n)
```
