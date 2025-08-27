# Solution for Problem 03: Area of a Rectangle

## Explanation
The area is calculated by multiplying length and width. Read the two integers and print their product.

---

### C++ Solution
```cpp
#include <iostream>

int main() {
    int length, width;
    std::cin >> length >> width;
    long long area = (long long)length * width;
    std::cout << area << std::endl;
    return 0;
}
```

### Python Solution
```python
length, width = map(int, input().split())
print(length * width)
```
