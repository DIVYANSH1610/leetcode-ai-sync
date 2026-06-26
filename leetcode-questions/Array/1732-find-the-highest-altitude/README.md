# 1732. Find the Highest Altitude

**Difficulty:** Easy
**Tags:** Array, Prefix Sum
**Language:** python

## Problem

See: https://leetcode.com/problems/find-the-highest-altitude/

## My Solution

See `solution.py`

## Approach
The solution iterates through all possible points where an altitude could be recorded, from the starting point to the end of the trip. For each point, it calculates the total altitude by summing all gain values from the beginning of the trip up to that point. It keeps track of the maximum altitude encountered throughout this process and returns it.

## Complexity
- Time: O(n^2)
- Space: O(1)

## Pattern
Brute Force

## Could it be improved?
Yes, the current solution can be significantly improved. The inner loop recalculates the sum of gains from the start for each altitude point, leading to O(n^2) time complexity. An optimal approach would be to maintain a running sum (current altitude). Initialize `current_altitude = 0` and `max_altitude = 0`. Iterate through the `gain` array once, adding each `gain` value to `current_altitude` and updating `max_altitude = max(max_altitude, current_altitude)` in each step. This would reduce the time complexity to O(n).
