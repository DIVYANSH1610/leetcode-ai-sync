# 3960. Frequency Balance Subarray

**Difficulty:** Medium
**Tags:** N/A
**Language:** python

## Problem

See: https://leetcode.com/problems/frequency-balance-subarray/

## My Solution

See `solution.py`

## Approach
The solution iterates through all possible subarrays by using nested loops for starting (`i`) and ending (`j`) indices. For each subarray, it maintains two frequency maps: `freq` stores the count of each number, and `freq_cnt` stores the count of each frequency value (e.g., if numbers 1 and 2 both appear 3 times, `freq_cnt[3]` would be 2). It updates these maps as `j` expands the subarray. The current subarray's length is considered for the maximum answer if it either contains only one distinct number, or if it contains exactly two distinct frequency values where one is twice the other.

## Complexity
- Time: O(N^2 * sqrt(N)) - The outer two loops run N and N times respectively. Inside the inner loop, updating `freq` and `freq_cnt` are O(1) on average. However, retrieving keys from `freq_cnt` using `freq_cnt.keys()` takes O(K) time where K is the number of distinct frequencies, which can be up to O(sqrt(N)).
- Space: O(N) - In the worst case, `freq` can store up to N distinct elements. `freq_cnt` stores at most O(sqrt(N)) distinct frequencies.

## Pattern
Brute-force Subarray Iteration / Nested Loops

## Could it be improved?
Yes, the solution can be improved to O(N^2) time complexity. The bottleneck is iterating through `freq_cnt.keys()` which takes O(sqrt(N)). Instead, a separate `set` can be maintained to explicitly track the distinct frequency values present in `freq_cnt`. When an element's frequency changes, the old frequency value is removed from this set (if its count in `freq_cnt` becomes zero), and the new frequency value is added. This makes the check for two frequencies and their values O(1) on average using `min()` and `max()` on the set, reducing the overall time complexity to O(N^2).
