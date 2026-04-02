# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        # step 1: walk to the node just before `left`
        before_left = dummy
        for _ in range(left - 1):
            before_left = before_left.next

        # step 2: reverse (right - left + 1) nodes
        prev = None
        curr = before_left.next
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        before_left.next.next = curr   
        before_left.next = prev       

        return dummy.next