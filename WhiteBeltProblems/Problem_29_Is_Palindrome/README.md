# Problem 29: Is Palindrome

## Problem Statement
Given a string, determine if it is a palindrome (reads the same forwards and backwards).

## Input
A single string `S`.

## Output
Print "Yes" if the string is a palindrome, "No" otherwise.

## Example
**Input:**
```
racecar
```

**Output:**
```
Yes
```

## Constraints
1 <= |S| <= 1000, S contains only lowercase letters.

## Explanation
Compare characters from the start and end, moving inward. If all pairs match, it’s a palindrome.
