# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        
        # Memoization dictionary to store results of subproblems
        # Key: (start, end), Value: List of unique BST roots
        memo = {}

        def generate(start: int, end: int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]
            
            if (start, end) in memo:
                return memo[(start, end)]
            
            unique_trees = []
            
            # Try every number 'i' as the root
            for i in range(start, end + 1):
                # Recursively generate all unique left subtrees
                left_trees = generate(start, i - 1)
                # Recursively generate all unique right subtrees
                right_trees = generate(i + 1, end)
                
                # Combine every left tree with every right tree
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        unique_trees.append(root)
            
            memo[(start, end)] = unique_trees
            return unique_trees

        return generate(1, n)