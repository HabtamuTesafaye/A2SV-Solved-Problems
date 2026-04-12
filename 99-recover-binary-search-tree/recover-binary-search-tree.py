class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = None
        second = None
        prev = None
        current = root
        
        while current:
            if not current.left:
                # Process current node
                if prev and prev.val > current.val:
                    if not first:
                        first = prev
                    second = current
                prev = current
                current = current.right
            else:
                # Find in-order predecessor
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                
                if not predecessor.right:
                    # First visit: create thread
                    predecessor.right = current
                    current = current.left
                else:
                    # Second visit: remove thread and process
                    predecessor.right = None
                    
                    if prev and prev.val > current.val:
                        if not first:
                            first = prev
                        second = current
                    prev = current
                    current = current.right
        
        # Swap values
        first.val, second.val = second.val, first.val