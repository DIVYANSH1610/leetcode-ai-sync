# 3612. Process String with Special Operations I

**Difficulty:** Medium
**Tags:** String, Simulation
**Language:** python

## Problem

See: https://leetcode.com/problems/process-string-with-special-operations-i/

## My Solution

See `solution.py`

## Approach
The solution processes the input string character by character, maintaining a dynamic list to store the actively processed characters. It directly simulates each operation specified in the problem description: appending regular characters to the list, popping the last character for a `'*'`, duplicating the entire list's contents for a `'#'`, and reversing the list in place for a `'%'`. Finally, the accumulated characters in the list are joined to form the output string.

## Complexity
- Time: The time complexity is dominated by the `extend` and `reverse` operations on the `res` list, which take time proportional to the current length of the list. In the worst-case scenario (e.g., an input string like `'a' + '#' * (N-1)`), the length of `res` can grow exponentially with `N`. This leads to a total time complexity of `O(N * L_max)`, where `L_max` is the maximum length `res` attains, which can be `O(2^N)`, making the overall time complexity `O(N * 2^N)`.
- Space: The space complexity is determined by the maximum length of the `res` list. In the worst case, this can also grow exponentially to `O(2^N)`.

## Pattern
Simulation

## Could it be improved?
Yes, for typical LeetCode constraints where `N` can be up to `10^5`, an `O(N * 2^N)` solution is prohibitively slow and memory-intensive. The operations `res.extend(res)` and `res.reverse()` are the primary bottlenecks. To achieve a more efficient solution (e.g., `O(N log N)` or `O(N)`), one would need a specialized data structure like a Rope or a segment tree for strings that supports efficient concatenation, splitting, duplication, and reversal operations, potentially using structural sharing or lazy propagation to avoid explicit copying of large character sequences.
