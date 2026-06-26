# 3962. Maximum Subarray Sum After at Most K Swaps

**Difficulty:** Hard
**Tags:** N/A
**Language:** python

## Problem

See: https://leetcode.com/problems/maximum-subarray-sum-after-at-most-k-swaps/

## My Solution

See `solution.py`

## Approach
The solution attempts to find the maximum subarray sum by iterating through all possible subarrays `nums[i...j]`. For each subarray, it aims to apply up to `k` operations to maximize the sum. The core idea for modifying the subarray is to identify negative numbers. A `dp[i][j]` table is intended to store the sum of negative numbers that *must remain* negative (i.e., not zeroed out) within `nums[i...j]`, after zeroing out up to `k` of the most negative values. This `dp[i][j]` is then subtracted from the original subarray sum. Additionally, the code tries to add the sum of `k` largest positive numbers found across various parts of the array, which is an incorrect step for a contiguous subarray sum problem.

## Complexity
- Time: O(N^2 log K) due to iterating through all `O(N^2)` subarrays and performing `O(log K)` heap operations for each.
- Space: O(N^2) for the `dp` table.

## Pattern
Dynamic Programming, Priority Queue / Min-Heap.

## Could it be improved?
Yes, the provided solution contains logical flaws.
1. The `dp[i][j]` calculation in the first set of loops is only assigned `sm` when `nums[j] >= 0`, leaving `dp[i][j]` uninitialized or incorrect for cases where `nums[j]` is negative. This should be fixed by consistently assigning `sm` to `dp[i][j]` after processing `nums[j]`.
2. The `cur += sm` component in the main iteration loop incorrectly adds `k` largest positive numbers from potentially non-contiguous parts of the array. This is not valid for a maximum *contiguous* subarray sum. This part should be removed.

Assuming the problem implies "change up to `k` negative numbers to `0` within the subarray", an `O(N^2 log K)` solution (by fixing the above flaws) is a straightforward approach. More optimal solutions exist: an `O(N * K)` dynamic programming approach (where `dp[i][j]` stores the maximum sum ending at `i` with `j` zeroed-out negatives) or an `O(N log N)` or `O(N log K)` solution using a sliding window combined with a data structure (like two heaps or a balanced BST) to efficiently track the sum of negatives within the window.
