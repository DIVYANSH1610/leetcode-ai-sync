# 1189. Maximum Number of Balloons

**Difficulty:** Easy
**Tags:** Hash Table, String, Counting
**Language:** python

## Problem

See: https://leetcode.com/problems/maximum-number-of-balloons/

## My Solution

See `solution.py`

## Approach
The solution attempts to construct the word "balloon" iteratively. In each iteration, it tries to find all required characters ('b', 'a', 'l', 'l', 'o', 'o', 'n') within the `text` string. Once a character is found, it is marked as used by replacing it with '#'. If all characters for "balloon" are successfully found, a counter is incremented, and the process repeats. If any required character cannot be found, the loop terminates, and the current count is returned.

## Complexity
- Time: O(N^2), where N is the length of the `text` string. In the worst case, the outer loop runs `O(N)` times, and in each iteration, it performs `O(len("balloon"))` searches, each of which can scan `O(N)` characters in the `text` list.
- Space: O(N), for converting the input string `text` into a list of characters.

## Pattern
Simulation

## Could it be improved?
Yes, significantly. The problem can be solved by counting character frequencies. First, count the occurrences of each character in the input `text`. Then, count the required occurrences of each character for the word "balloon" (e.g., 'b':1, 'a':1, 'l':2, 'o':2, 'n':1). The maximum number of "balloon" words that can be formed is limited by the character that runs out first, so it's the minimum of (count of 'b' / 1), (count of 'a' / 1), (count of 'l' / 2), (count of 'o' / 2), and (count of 'n' / 1). This improved approach would have a time complexity of O(N) and space complexity of O(1) (since the character set is fixed and small).
