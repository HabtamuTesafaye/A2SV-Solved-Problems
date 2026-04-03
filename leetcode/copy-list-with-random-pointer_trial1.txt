"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        current = head
        while current:
            copy = Node(current.val)
            copy.next = current.next
            current.next = copy
            current = copy.next

        current2 = head
        while current2:
            if current2.random:
                current2.next.random = current2.random.next
            current2 = current2.next.next
        
        current3 = head
        copy_head = head.next

        while current3:
            copy_val = current3.next
            current3.next = copy_val.next
            if copy_val.next:
                copy_val.next = copy_val.next.next
            current3 = current3.next

        return copy_head


        



        