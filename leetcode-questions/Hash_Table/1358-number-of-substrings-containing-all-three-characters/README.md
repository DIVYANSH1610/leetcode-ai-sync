# 1358. Number of Substrings Containing All Three Characters

**Difficulty:** Medium
**Tags:** Hash Table, String, Sliding Window
**Language:** python

## Problem

See: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

## My Solution

See `solution.py`

## Approach
This solution uses a sliding window approach. It keeps track of the most recent indices of the characters 'a', 'b', and 'c'. For each character encountered, it updates its last seen index. The number of valid substrings ending at the current index is determined by the minimum of these last seen indices, representing the start of the earliest possible valid substring.

## Complexity
- Time: O(n)
- Space: O(1)

## Pattern
Sliding Window

## Could it be improved?
The current approach is already optimal with a linear time and constant space complexity.
