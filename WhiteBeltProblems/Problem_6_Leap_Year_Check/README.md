# Problem 6: Leap Year Check

## Problem Statement
Given a year, determine if it is a leap year. A year is a leap year if it is divisible by 4, except for end-of-century years, which must be divisible by 400.

## Input
A single integer `year`.

## Output
Print "Yes" or "No".

## Example
**Input:**
```
2000
```

**Output:**
```
Yes
```

## Constraints
1 <= year <= 10000

## Explanation
A year is a leap year if `(year % 4 == 0 AND year % 100 != 0) OR (year % 400 == 0)`.
