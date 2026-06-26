# 3737. Count Subarrays With Majority Element I

**Difficulty:** Medium
**Tags:** Array, Hash Table, Divide and Conquer, Segment Tree, Merge Sort, Counting, Prefix Sum
**Language:** python

## Problem

See: https://leetcode.com/problems/count-subarrays-with-majority-element-i/

## My Solution

See `solution.py`

## Approach
The solution iterates through all possible subarrays of the input array `nums` using nested loops. For each subarray, it counts the occurrences of the `target` element. If the `target` count for a given subarray is strictly greater than half the subarray's length, the subarray is considered a "majority subarray," and the total count is incremented.

## Complexity
- Time: O(n^2)
- Space: O(1)

## Pattern
Brute Force

## Could it be improved?
Yes, the current O(n^2) approach can be improved to O(n log n) or potentially O(n). The problem can be transformed by mapping `target` elements to `1` and all other elements to `-1`. The condition `target_count > length // 2` then becomes equivalent to finding subarrays whose sum is strictly positive in this transformed array. This can be solved by computing prefix sums and using a data structure like a Fenwick tree or a balanced binary search tree (after coordinate compression of prefix sums) to efficiently count previous prefix sums that are less than the current one.
