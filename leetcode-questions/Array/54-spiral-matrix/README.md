# 54. Spiral Matrix

**Difficulty:** Medium
**Tags:** Array, Matrix, Simulation
**Language:** python

## Problem

See: https://leetcode.com/problems/spiral-matrix/

## My Solution

See `solution.py`

## Approach
The solution simulates the spiral traversal by maintaining four pointers: `top`, `bottom`, `left`, and `right`, which define the current boundaries of the unvisited portion of the matrix. It iteratively traverses the elements of the outermost layer of the remaining matrix in a clockwise direction (right, down, left, up), then shrinks the respective boundary pointers. This process continues as long as `top` is less than or equal to `bottom` and `left` is less than or equal to `right`, ensuring all elements are visited.

## Complexity
- Time: O(m * n), where `m` is the number of rows and `n` is the number of columns. Each element in the matrix is visited and appended to the result exactly once.
- Space: O(m * n), to store all `m * n` elements of the matrix in the `res` list as required by the problem output.

## Pattern
Simulation

## Could it be improved?
The current approach is optimal in terms of both time and space complexity. Since every element must be visited and returned in the result list, O(m*n) time and O(m*n) space are the theoretical minimums, which this solution achieves. There is no fundamentally more efficient algorithmic solution for this problem.
