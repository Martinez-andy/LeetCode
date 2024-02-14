# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        return (self.sameTree(root, subRoot) 
        or self.isSubtree(root.left, subRoot)
        or self.isSubtree(root.right, subRoot))

    def sameTree(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
        if not (tree1 or tree2):
            return True
        elif (not tree1 and tree2) or (not tree2 and tree1):
            return False
        
        return (tree1.val == tree2.val 
                and self.sameTree(tree1.left, tree2.left)
                and self.sameTree(tree1.right, tree2.right))

"""
    Sketch:
        Tree objects are different, must then compare values and
        structure rather than comparing using ==.

        Maybe use DFS or BFS?
"""