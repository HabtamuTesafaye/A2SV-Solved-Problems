"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        current = head
        while current:
            if current.child:
                next_node = current.next


                child_head = current.child

                # link the child head
                current.next = child_head
                child_head.prev = current
                current.child = None

                # find tail and assign value 
                dummy = child_head
                while dummy.next:
                    dummy = dummy.next

                # link the child tail
                if next_node:
                    dummy.next = next_node
                    next_node.prev = dummy

            current = current.next

        return head
