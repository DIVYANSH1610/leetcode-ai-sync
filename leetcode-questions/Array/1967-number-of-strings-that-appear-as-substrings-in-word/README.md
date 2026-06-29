# 1967. Number of Strings That Appear as Substrings in Word

**Difficulty:** Easy
**Tags:** Array, String
**Language:** python

## Problem

See: https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

## My Solution

See `solution.py`

## Approach
The solution iterates through each pattern in the given list of patterns. For each pattern, it checks if that pattern exists as a substring within the target word. If a pattern is found as a substring, a counter is incremented. Finally, the total count of patterns found as substrings is returned.

## Complexity
- Time: O(N * M * K) where N is the number of patterns, M is the length of the `word`, and K is the average length of a pattern. The `in` operator for strings in Python has a time complexity proportional to the product of the lengths of the string being searched and the substring.
- Space: O(1)

## Pattern
Substring Search

## Could it be improved?
The provided solution is straightforward and likely sufficient for the "Easy" difficulty. However, for very large inputs, a more optimized substring search algorithm like Knuth-Morris-Pratt (KMP) or Rabin-Karp could improve the time complexity. These algorithms preprocess the patterns or use hashing to significantly reduce the average time taken to search for multiple patterns within a single text.
