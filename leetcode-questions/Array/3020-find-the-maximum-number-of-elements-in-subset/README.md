# 3020. Find the Maximum Number of Elements in Subset

**Difficulty:** Medium
**Tags:** Array, Hash Table, Enumeration
**Language:** python

## Problem

See: https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

## My Solution

See `solution.py`

## Approach
The core idea is to consider each number as a potential starting point of a subsequence where each element is the square of the previous one. For each starting number, we count how many elements of its squared sequence (e.g., x, x*x, x*x*x*x, ...) are present in the input array with a frequency of at least 2. We also account for a single occurrence of the last element in the sequence if it exists. The maximum length found across all starting numbers is the answer.

## Complexity
- Time: O(N log M) where N is the number of unique elements and M is the maximum value in nums. The outer loop iterates through unique elements, and the inner while loop's iterations are logarithmic with respect to M due to squaring. In the worst case, this can be O(N * log(max(nums))).
- Space: O(U) where U is the number of unique elements in `nums` for storing the frequency map.

## Pattern
Greedy, Iteration

## Could it be improved?
The current approach is efficient and likely optimal for the given constraints. The greedy strategy of extending sequences from each unique number that appears at least twice is sound.
