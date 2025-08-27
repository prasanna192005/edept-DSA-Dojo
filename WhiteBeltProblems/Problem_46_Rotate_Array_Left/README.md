# Problem 46: Rotate Array Left

## Problem Statement
Rotate an array of `N` integers left by `K` positions.

## Input
The first line contains `N` and `K`. The second line contains `N` space-separated integers.

## Output
The array after rotating left by `K` positions, space-separated.

## Example
**Input:**
```
5 2
1 2 3 4 5
```

**Output:**
```
3 4 5 1 2
```

## Constraints
1 <= N <= 1000, 0 <= K <= N, -10^6 <= array elements <= 10^6

## Explanation
Shift each element left by `K` positions, wrapping around to the end. Use modulo to handle the rotation.
