# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        first_partition_dummy = ListNode(0)
        second_partition_dummy = ListNode(0)

        first_partition = first_partition_dummy
        second_partition = second_partition_dummy

        current = head
        while current:
            if current.val < x:
                first_partition.next = current
                first_partition =  first_partition.next
            else:
                second_partition.next = current
                second_partition =  second_partition.next

            current = current.next
        
        second_partition.next = None
        first_partition.next = second_partition_dummy.next

        return first_partition_dummy.next