"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        # Start from the root of the tree
        head = root
        
        while head:
            # Dummy node to simplify the logic for the next level
            dummy = Node(0)
            tail = dummy
            
            # Traverse the current level using the 'next' pointers
            curr = head
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                
                curr = curr.next
            
            # Move to the next level
            head = dummy.next
        
        return root