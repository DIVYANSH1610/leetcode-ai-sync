# 2812. Find the Safest Path in a Grid

**Difficulty:** Medium
**Tags:** Array, Binary Search, Breadth-First Search, Union-Find, Heap (Priority Queue), Matrix
**Language:** python

## Problem

See: https://leetcode.com/problems/find-the-safest-path-in-a-grid/

## My Solution

See `solution.py`

## Approach
The problem asks for the maximum minimum distance from any thief to any cell on a path from the top-left to the bottom-right. This can be solved in two phases. First, a multi-source BFS is used to calculate the minimum distance from each cell to the nearest thief. This distance essentially represents the "safeness" of that cell. Second, a modified Dijkstra's algorithm (implemented with a max-heap) is used to find the path from (0,0) to (n-1, n-1) that maximizes this minimum safeness value.

## Complexity
- Time: O(N^2 * log(N^2)) where N is the dimension of the grid. The BFS takes O(N^2) and the Dijkstra with a priority queue takes O(E log V), where V=N^2 and E is at most 4*N^2.
- Space: O(N^2) for storing the scores and visited array, and for the priority queue.

## Pattern
Two BFS, Max Heap (Dijkstra's Variant)

## Could it be improved?
The current approach using a priority queue for the second phase results in O(N^2 log(N^2)) time complexity. This can be improved by observing that the "safeness" values are integers within a limited range (0 to N^2-1). A binary search can be performed on the possible answer (the minimum safeness factor). For each candidate safeness factor `k`, we can check if a path exists where every cell has a safeness of at least `k` using a simple BFS or DFS. This reduces the time complexity to O(N^2 * log(N^2)), where the log factor comes from the binary search on the possible safeness values.
