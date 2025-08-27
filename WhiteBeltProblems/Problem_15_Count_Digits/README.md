# Problem 15: Count Digits

## Problem Statement
Count the number of digits in a given integer.

## Input
A single integer `N`.

## Output
The number of digits in `N`.

## Example
**Input:**
```
12345
```

**Output:**
```
5
```

## Constraints
0 <= N <= 1,000,000,000

## Explanation
Use a while loop. Repeatedly divide the number by 10 and increment a counter until the number becomes 0. A special case is input 0, which has 1 digit.
