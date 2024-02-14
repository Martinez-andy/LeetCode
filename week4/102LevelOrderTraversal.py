# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        prev = [root] if root else []
        res = []
        curr = []

        while prev:
            prev, curr = [], prev
            res.append([])
            for node in curr:
                res[-1].append(node.val)
                if node.left:
                    prev.append(node.left)
                if node.right:
                    prev.append(node.right)
        return res
"""

    Sketch:
        Have three lists:
            1.) One contains the previous values
            2.) One contains the current values
            3.) The last one is the return value

        Start by populating previous with the root node
        
        Enter a loop, set curr = prev and then reset prev

        For each node in curr...
            1.) Add any non-null node values to last slot in res
            2.) Add any nodes connected to curr node into prev (left then right)


    Since we want to print out the tree by level, I think a BFS would be 
    our best bet.

    Run BFS to traverse through tree by level
    Store previous nodes in a list
    Pop from prev to create new list

"""

"""
    COULD ALSO SOLVE USING A SINGLE QUEUE
"""

"""
    Notes:
        When we want to execute in order traversal of a BT we want to use BFS.
        BFS is implemented with a queue and DFS is implemented with a stack.
"""