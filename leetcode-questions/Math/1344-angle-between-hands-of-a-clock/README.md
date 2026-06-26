# 1344. Angle Between Hands of a Clock

**Difficulty:** Medium
**Tags:** Math
**Language:** python

## Problem

See: https://leetcode.com/problems/angle-between-hands-of-a-clock/

## My Solution

See `solution.py`

## Approach
The solution calculates the angular position of both the hour and minute hands independently, relative to the 12 o'clock mark. The minute hand moves 6 degrees per minute, while the hour hand moves 30 degrees per hour, plus an additional 0.5 degrees for every minute passed. The absolute difference between these two angles gives one of the two possible angles between the hands, and the function then returns the smaller of this difference and (360 degrees minus the difference).

## Complexity
- Time: O(1)
- Space: O(1)

## Pattern
Math / Direct Calculation

## Could it be improved?
The approach is already optimal, achieving constant time and space complexity. No further algorithmic improvements are possible as the solution involves a fixed number of arithmetic operations to derive the result.
