# Problem 34: First Non-Repeating Character

## Problem Statement
Find the first non-repeating character in a string.

## Input
A single string `S`.

## Output
The first non-repeating character, or "None" if none exists.

## Example
**Input:**
```
aabbcc
```

**Output:**
```
None
```

## Constraints
1 <= |S| <= 1000, S contains only lowercase letters.

## Explanation
Use an array or hash map to count character frequencies, then find the first character with a count of 1.
