# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy head to simplify code
        current = dummy
        carry = 0

        # Traverse both lists until both are None
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # Value from l1 or 0
            val2 = l2.val if l2 else 0  # Value from l2 or 0

            total = val1 + val2 + carry
            carry = total // 10  # Carry for next digit
            current.next = ListNode(total % 10)  # Current digit

            # Move pointers forward
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next