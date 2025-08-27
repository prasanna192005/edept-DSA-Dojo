# Problem 40: Binary to Decimal

## Problem Statement
Convert a binary string to its decimal equivalent.

## Input
A string `S` representing a binary number.

## Output
The decimal equivalent of the binary number.

## Example
**Input:**
```
1010
```

**Output:**
```
10
```

## Constraints
1 <= |S| <= 32, S contains only 0s and 1s.

## Explanation
Iterate through the string, multiplying each bit by the corresponding power of 2 and summing the results.
