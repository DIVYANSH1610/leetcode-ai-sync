# 3699. Number of ZigZag Arrays I

**Difficulty:** Hard
**Tags:** Dynamic Programming, Prefix Sum
**Language:** python

## Problem

See: https://leetcode.com/problems/number-of-zigzag-arrays-i/

## My Solution

See `solution.py`

## Approach
This solution uses dynamic programming to count zigzag arrays. It maintains a 1D DP array, `dp`, where `dp[k]` represents the number of zigzag arrays of the current length ending with the `k`-th smallest value in `[l, r]` and whose last step was strictly increasing. Due to the inherent symmetry of zigzag patterns, the number of arrays ending with a decreasing last step can be derived from the increasing counts. Each iteration builds the counts for length `i` based on length `i-1` by applying prefix sums after reversing the `dp` array, effectively switching between increasing-ending and decreasing-ending states.

## Complexity
- Time: O(N * M), where `M = r - l + 1` is the number of possible values for array elements. Each of the `N-1` iterations involves reversing an array of size `M` and then performing `M` constant-time operations for prefix sums.
- Space: O(M), for storing the `dp` array.

## Pattern
Dynamic Programming - 1D, Prefix Sum

## Could it be improved?
Yes, the time complexity can be improved for very large `N`. The state transitions (prefix/suffix sums) are linear transformations, which can be represented as matrix multiplications. By formulating the DP recurrence as `Vec_i = Matrix * Vec_{i-1}`, matrix exponentiation by squaring can compute `Matrix^(N-1)` in `O(M^3 * log N)` time. This approach would be significantly faster if `N` is much larger than `M^2`.
