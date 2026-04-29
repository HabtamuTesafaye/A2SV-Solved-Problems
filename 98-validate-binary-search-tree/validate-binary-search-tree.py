# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            # Base case: empty tree is a valid BST
            if not node:
                return True
        
            # Current node must be strictly within the range (low, high)
            if not (low < node.val < high):
                return False
            
            # Recursively validate left and right subtrees with updated ranges
            # Left child: max becomes current node's value
            # Right child: min becomes current node's value
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))

        # Start with the widest possible range
        return validate(root, float('-inf'), float('inf'))