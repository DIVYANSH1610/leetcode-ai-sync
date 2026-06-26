# 2130. Maximum Twin Sum of a Linked List

**Difficulty:** Medium
**Tags:** Linked List, Two Pointers, Stack
**Language:** python

## Problem

See: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

## My Solution

See `solution.py`

## Approach
This solution uses the fast and slow pointer technique to efficiently locate the middle of the linked list. As the slow pointer traverses the first half of the list, it stores the value of each node in a temporary list. Once the slow pointer reaches the start of the second half, the algorithm iterates through this second half while simultaneously popping values from the temporary list. The temporary list, acting as a stack, provides the values from the first half in reverse order, which are precisely the "twin" nodes needed to calculate the sum, and the maximum sum is tracked and returned.

## Complexity
- Time: O(N)
- Space: O(N)

## Pattern
Two Pointers, Stack

## Could it be improved?
Yes, the space complexity can be improved to O(1). This can be achieved by using fast and slow pointers to find the middle, then reversing the second half of the linked list in place. After reversing, you can iterate with one pointer from the original head and another from the head of the reversed second half, calculating twin sums and finding the maximum. Finally, the second half can be reversed again to restore the list's original structure.
