# 3559. Number of Ways to Assign Edge Weights II

**Difficulty:** Hard
**Tags:** Array, Math, Dynamic Programming, Bit Manipulation, Tree, Depth-First Search
**Language:** python

## Problem

See: https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

## My Solution

See `solution.py`

## Approach
The solution first constructs a tree from the given edges. It then precomputes the depths of all nodes and their ancestors at powers of two using binary lifting. For each query, it efficiently finds the Lowest Common Ancestor (LCA) of the two queried nodes. The number of edges in the path between the nodes is derived from their depths and the LCA's depth, and this path length is then used in a `pow(2, edges_in_path - 1, MOD)` formula to calculate the final answer.

## Complexity
- Time: O(N log N + Q log N), where N is the number of nodes (V) and Q is the number of queries. N log N time is spent on precomputing ancestor information for binary lifting, and Q log N time is spent on answering all queries.
- Space: O(N log N), primarily for storing the binary lifting parent array.

## Pattern
Tree Algorithms, Lowest Common Ancestor (LCA) - Binary Lifting

## Could it be improved?
The approach is optimal for answering multiple LCA queries on a static tree using binary lifting. While an alternative approach using an Euler tour and a Sparse Table (for Range Minimum Query) could achieve O(N) precomputation and O(1) query time for LCA, the O(N log N) precomputation and O(log N) query time of binary lifting is highly efficient and generally sufficient for typical competitive programming constraints, offering a good balance between performance and implementation simplicity.
