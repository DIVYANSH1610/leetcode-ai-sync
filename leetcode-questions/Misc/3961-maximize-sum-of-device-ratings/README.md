# 3961. Maximize Sum of Device Ratings

**Difficulty:** Medium
**Tags:** N/A
**Language:** python

## Problem

See: https://leetcode.com/problems/maximize-sum-of-device-ratings/

## My Solution

See `solution.py`

## Approach
The solution first processes each device by sorting its unit ratings to easily identify the smallest (`row[0]`) and second smallest (`row[1]`) ratings. It then accumulates the sum of all second smallest ratings across all devices, simultaneously tracking the single globally minimum first rating and the single globally minimum second rating found. The final result is computed by taking the total sum of second smallest ratings, subtracting the globally minimum second rating, and adding the globally minimum first rating.

## Complexity
- Time: O(R * n log n) where R is the number of devices (rows in `units`) and n is the number of units per device. This is due to sorting each of the R rows, which takes O(n log n) per row.
- Space: O(n) due to the auxiliary space used by Python's `list.sort()` (Timsort) for sorting each row. The other variables use O(1) space.

## Pattern
Sorting, Array Processing

## Could it be improved?
The current approach is optimal for performing the specific calculation implied by the return statement (`sum_seconds - smallest_second + smallest_first`). Sorting each device's ratings to find the two smallest elements is typically O(n log n) per device if `n` can be large. The subsequent aggregation and final calculation are performed efficiently in O(R) time. Thus, the overall time complexity of O(R * n log n) is efficient for the required task.
