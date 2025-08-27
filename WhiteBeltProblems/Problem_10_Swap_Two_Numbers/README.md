# Problem 10: Swap Two Numbers

## Problem Statement
Given two integers, `a` and `b`, swap their values and print them.

## Input
Two space-separated integers `a` and `b`.

## Output
Two space-separated integers, with values swapped.

## Example
**Input:**
```
10 20
```

**Output:**
```
20 10
```

## Constraints
-1,000,000,000 <= a, b <= 1,000,000,000

## Explanation
Use a third temporary variable to hold one value while you perform the swap. Python allows for direct tuple assignment `a, b = b, a`.
