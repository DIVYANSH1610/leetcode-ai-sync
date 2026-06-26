# 1840. Maximum Building Height

**Difficulty:** Hard
**Tags:** Array, Math, Sorting
**Language:** python

## Problem

See: https://leetcode.com/problems/maximum-building-height/

## My Solution

See `solution.py`

## Approach
The solution first preprocesses the given restrictions by inserting a virtual building at index 1 with height 0, then sorting all restrictions by building ID. It then performs two passes: a left-to-right pass and a right-to-left pass. These passes update the maximum allowable height for each restricted building, ensuring all slope constraints (height difference at most distance difference) are met between adjacent restricted buildings. Finally, it iterates through these refined restricted points, calculating the maximum possible height in each segment between them (including segments from building 1 to the first restriction and from the last restriction to building `n`), using a geometric formula for the peak height in a triangle bounded by slope 1.

## Complexity
- Time: O(M log M) where M is the number of restrictions. This is dominated by sorting the restrictions.
- Space: O(M) for storing and modifying the restrictions.

## Pattern
Two-pass DP, Geometric

## Could it be improved?
The approach is optimal in terms of computational complexity. Given that the restrictions are not guaranteed to be sorted, an O(M log M) time complexity is the best achievable due to the sorting requirement. The subsequent passes and calculations are all linear, O(M). Since `M` is much smaller than `n`, this approach correctly avoids iterating through `n` buildings directly.
