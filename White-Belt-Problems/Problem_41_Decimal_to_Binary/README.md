# Problem 41: Decimal to Binary

## Problem Statement
Convert a decimal number to its binary representation.

## Input
A single integer `N`.

## Output
The binary representation of `N`.

## Example
**Input:**
```
10
```

**Output:**
```
1010
```

## Constraints
0 <= N <= 10^9

## Explanation
Repeatedly divide the number by 2, collecting remainders in reverse order to form the binary string.
