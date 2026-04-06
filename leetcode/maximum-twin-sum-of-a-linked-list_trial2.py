# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # pair from both ends
        res = 0
        left, right = head, prev
        while right:
            res = max(res, left.val + right.val)
            left = left.next
            right = right.next

        return res