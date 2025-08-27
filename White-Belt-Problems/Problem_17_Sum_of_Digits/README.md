# Problem 17: Sum of Digits

## Problem Statement
Given an integer `N`, calculate the sum of its digits.

## Input
A single integer `N`.

## Output
The sum of digits of `N`.

## Example
**Input:**
```
123
```

**Output:**
```
6
```

## Constraints
0 <= N <= 1,000,000,000

## Explanation
Extract each digit using modulo (`% 10`) and division (`/ 10`), or convert to a string and sum the characters as integers.
