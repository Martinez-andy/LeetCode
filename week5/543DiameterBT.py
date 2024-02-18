# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal diameter
            if not root:
                return -1
            left = dfs(root.left) + 1
            right = dfs(root.right) + 1
            diameter = max(diameter, left + right)
            return max(left, right)
        dfs(root)
        return diameter

    """
        Leverage DFS but only return once we reach a leaf node.
        Note, this 
    """
    
    # Run a DFS alg to find the maximum depth
    # Set max equal to the maximum between the diameters of both sides
    # Return that value plus 1