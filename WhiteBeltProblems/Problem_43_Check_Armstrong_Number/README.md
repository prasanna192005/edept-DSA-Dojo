# Problem 43: Check Armstrong Number

## Problem Statement
Determine if a number is an Armstrong number (sum of its digits raised to the power of the number of digits equals the number).

## Input
A single integer `N`.

## Output
Print "Yes" if `N` is an Armstrong number, "No" otherwise.

## Example
**Input:**
```
153
```

**Output:**
```
Yes
```

## Constraints
1 <= N <= 10^9

## Explanation
Count the number of digits, then compute the sum of each digit raised to that power. Compare with the original number.
