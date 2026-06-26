# 1499. Max Value of Equation

**Difficulty:** Hard
**Tags:** Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue
**Language:** python

## Problem

See: https://leetcode.com/problems/max-value-of-equation/

## My Solution

See `solution.py`

## Approach
This solution iterates through the given points, treating each point `j` as the rightmost point in a potential pair `(i, j)`. For each `j`, it uses a monotonic deque to efficiently find the optimal `i` such that `i < j`, `points[j][0] - points[i][0] <= k`, and `points[i][1] - points[i][0]` is maximized. The deque maintains `(points[i][1] - points[i][0], points[i][0])` pairs in decreasing order of `points[i][1] - points[i][0]`, and filters out invalid `i`s based on the `k` constraint or if a newer `j` provides a better `points[j][1] - points[j][0]` value.

## Complexity
- Time: O(N), where N is the number of points. Each point is added to and removed from the deque at most once.
- Space: O(N), in the worst case, all points might be stored in the deque.

## Pattern
Monotonic Queue (Sliding Window)

## Could it be improved?
The approach is already optimal. It processes each point in constant amortized time, leading to an overall O(N) time complexity, which is the best possible as every point must be examined. The space complexity is also optimal for this approach given the need to potentially store elements within the sliding window.
