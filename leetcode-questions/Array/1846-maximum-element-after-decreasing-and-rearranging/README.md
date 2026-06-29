# 1846. Maximum Element After Decreasing and Rearranging

**Difficulty:** Medium
**Tags:** Array, Greedy, Sorting
**Language:** python

## Problem

See: https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

## My Solution

See `solution.py`

## Approach
The problem asks us to find the largest possible value for the maximum element after applying two operations: decreasing any element and rearranging the array. The key insight is that to maximize the largest element, we should aim to make the elements as close to their indices as possible. By sorting the array and then iterating, we ensure that each element is at most one greater than the previous element, effectively filling the array greedily from left to right with increasing values.

## Complexity
- Time: O(N log N) due to sorting.
- Space: O(1) if sorting is in-place, or O(N) if a copy is made for sorting.

## Pattern
Greedy

## Could it be improved?
The current approach is already optimal. The sorting step dominates the time complexity, and there's no way to solve this without considering the relative order or magnitude of elements, which sorting efficiently handles.
