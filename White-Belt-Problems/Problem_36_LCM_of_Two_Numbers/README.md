# Problem 36: LCM of Two Numbers

## Problem Statement
Find the least common multiple (LCM) of two positive integers.

## Input
Two space-separated integers `a` and `b`.

## Output
The LCM of `a` and `b`.

## Example
**Input:**
```
6 8
```

**Output:**
```
24
```

## Constraints
1 <= a, b <= 10^9

## Explanation
Use the formula LCM(a, b) = (a * b) / GCD(a, b). Compute GCD using the Euclidean algorithm.
