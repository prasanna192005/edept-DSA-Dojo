# Problem 35: GCD of Two Numbers

## Problem Statement
Find the greatest common divisor (GCD) of two positive integers using the Euclidean algorithm.

## Input
Two space-separated integers `a` and `b`.

## Output
The GCD of `a` and `b`.

## Example
**Input:**
```
48 18
```

**Output:**
```
6
```

## Constraints
1 <= a, b <= 10^9

## Explanation
Use the Euclidean algorithm: GCD(a, b) = GCD(b, a % b) until b becomes 0.
