# 2095. Delete the Middle Node of a Linked List

**Difficulty:** Medium
**Tags:** Linked List, Two Pointers
**Language:** python

## Problem

See: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

## My Solution

See `solution.py`

## Approach
This solution employs the classic two-pointer technique to efficiently locate the node preceding the middle node. A slow pointer advances one step at a time, while a fast pointer advances two steps. By initializing the slow pointer at the head and the fast pointer at `head.next.next`, the slow pointer naturally lands on the node just before the target middle node when the fast pointer reaches the end of the list or `None`. Finally, the middle node is "deleted" by updating the `next` pointer of the preceding node to skip over it.

## Complexity
- Time: O(N) where N is the number of nodes in the linked list. Both slow and fast pointers traverse the list, with the fast pointer making at most N/2 steps.
- Space: O(1) as only a constant number of extra variables are used, irrespective of the list size.

## Pattern
Two Pointers

## Could it be improved?
No, the approach is already optimal. It solves the problem in a single pass through the linked list with constant extra space, which is the best possible complexity for this problem.
