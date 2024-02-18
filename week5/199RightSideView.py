# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:\
        if not root: return []
        search = [root]
        res = []
        while search:
            temp = []
            maxLen = len(search)
            for i in range(maxLen - 1, -1, -1):
                curr = search.pop()
                if i == maxLen - 1:
                    res.append(curr.val)
                if curr.right:
                    temp = [curr.right] + temp
                if curr.left:
                    temp = [curr.left] + temp
            search = temp
        return res

"""
    Solution notes:
        Note, whenever a tree question's answer depends on the level
    of each set of nodes, then use BFS instead of DFS. These questions 
    likely require a modification of the BFS alg but most of the algorithm
    should apply.
"""