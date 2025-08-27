# Problem 30: Uppercase to Lowercase

## Problem Statement
Given a string of uppercase letters, convert it to lowercase and print it.

## Input
A single string `S`.

## Output
The string converted to lowercase.

## Example
**Input:**
```
HELLO
```

**Output:**
```
hello
```

## Constraints
1 <= |S| <= 1000, S contains only uppercase letters.

## Explanation
Iterate through the string and convert each character by adding 32 to its ASCII value, or use a built-in lowercase function.
