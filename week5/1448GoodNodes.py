# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Initialize our return value
        res = 0
        def dfs(root: TreeNode, maximum: int):
            if not root:
                return None
            nonlocal res

            if root.val >= maximum:
                res += 1
                maximum = max(maximum, root.val)
            dfs(root.left, maximum)
            dfs(root.right, maximum)
        dfs(root, root.val)
        return res

"""
    Solution notes:
        Realize that you only need to worry about the maximum value so far
    when traversing the tree. Thus, run a modified DFS with a maximum value
    as an arguement. Then, only increment the non-local result variable if 
    the condition root.val >= maximum is met. Don't forget to handle the base
    case of a leaf node because we are using recursion.

    Side notes:
        Could also implement the dfs alg to return a result variable instead of 
    updating a non-local variable. Doing this would mean you can just return
    dfs(root, root.val).
"""