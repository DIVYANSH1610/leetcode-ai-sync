# 3959. Check Good Integer

**Difficulty:** Easy
**Tags:** N/A
**Language:** python

## Problem

See: https://leetcode.com/problems/check-good-integer/

## My Solution

See `solution.py`

## Approach
The solution iterates through each digit of the input integer `n` from right to left. In each step, it extracts the last digit using the modulo operator and updates two cumulative sums: the sum of the digits and the sum of the squares of the digits. The number `n` is then reduced by integer division until it becomes zero. Finally, it checks if the difference between the sum of squares and the sum of digits meets the specified threshold.

## Complexity
- Time: O(log N)
- Space: O(1)

## Pattern
Digit Manipulation

## Could it be improved?
The current approach is optimal for this problem. It directly computes the necessary sums by iterating through each digit once, achieving O(log N) time complexity and O(1) space complexity. There are no asymptotic improvements possible as all digits must be examined to evaluate the given condition.
