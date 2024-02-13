# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root: Optional[TreeNode], left, right) -> bool:
            if not root:
                return True
            return (left < root.val 
            and root.val < right 
            and valid(root.left, left, root.val) 
            and valid(root.right, root.val, right))
        return valid(root, float("-inf"), float("inf"))


# Instead of thinking bottom up, try thinking top down
"""
    Definition of binary tree relies on 
        1.) Root must be greater than all elements on left child
        2.) Root must be less than all elements on right child

    These rules can be reframed to be:
        1.) All elements of left child must be less than root
        2.) All element of right child must be greater than root
"""