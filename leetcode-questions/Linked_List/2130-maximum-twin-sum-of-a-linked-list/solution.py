class Solution:
    def pairSum(self, head):
        half = []
        slow = fast = head

        while fast and fast.next:
            half.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        res = 0
        while slow:
            res = max(res, half.pop() + slow.val)
            slow = slow.next

        return res