# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        current = head 
        while current:
            length += 1
            current = current.next

        width = length // k
        reimider = length % k

        result = []
        curr = head
        for i in range(k):
            part_head= curr
            size = width + (1 if i < reimider else 0 )
            for j in range(size - 1):
                if curr:
                    curr = curr.next
            
            if curr:
                next_node = curr.next
                curr.next = None
                curr = next_node

            result.append(part_head)
        
        return result
