# 3739. Count Subarrays With Majority Element II

**Difficulty:** Hard
**Tags:** Array, Hash Table, Divide and Conquer, Segment Tree, Merge Sort, Prefix Sum
**Language:** python

## Problem

See: https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

## My Solution

See `solution.py`

## Approach
The problem asks us to count subarrays where a specific `target` element is the majority element. We can transform the array by replacing `target` with `1` and all other elements with `-1`. A subarray has `target` as the majority if the sum of these transformed values within the subarray is strictly positive. We then use a prefix sum array to efficiently calculate subarray sums and a frequency map (implemented as an array `freq`) to count occurrences of prefix sums. By iterating through the prefix sums, we can determine how many subarrays ending at the current index have a positive sum.

## Complexity
- Time: O(N)
- Space: O(N)

## Pattern
Prefix Sum, Hash Table (implicitly through frequency array)

## Could it be improved?
The current O(N) time and O(N) space solution is optimal. The use of prefix sums and a frequency map allows for a single pass through the array to count the valid subarrays.
