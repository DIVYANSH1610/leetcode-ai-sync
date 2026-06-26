# 1833. Maximum Ice Cream Bars

**Difficulty:** Medium
**Tags:** Array, Greedy, Sorting, Counting Sort
**Language:** python

## Problem

See: https://leetcode.com/problems/maximum-ice-cream-bars/

## My Solution

See `solution.py`

## Approach
The solution first builds a frequency map (or array) of ice cream bar costs, counting how many bars are available at each specific price. Then, it iterates through the possible prices in ascending order, starting from the cheapest. For each price, it buys as many ice cream bars as possible given the available coins and the number of bars at that price, updating the total count and remaining coins until no more bars can be afforded.

## Complexity
- Time: O(N + max_cost), where N is the number of ice cream bars and max_cost is the maximum cost of an ice cream bar.
- Space: O(max_cost), for storing the frequency array.

## Pattern
Greedy, Counting Sort

## Could it be improved?
The current approach is optimal for the given constraints. It uses a counting sort-like mechanism to efficiently process the ice cream bars by cost, achieving a linear time complexity proportional to the number of bars plus the maximum possible cost, which is often superior to a general comparison sort (O(N log N)) when the maximum cost is within a similar magnitude as N.
