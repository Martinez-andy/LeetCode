class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        count = 0

        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            count += 1
            curr = stack.pop()
            if count == k:
                return curr.val
            curr = curr.right
            
"""
    Notes:
        Knew to use some sort of backtracking/DFS, turns out in order traversal was the way.
        Used a stack and a while loop to implement in order traversal iteratively. Stack
        allowed me to back track up the tree without needing recursion. Additionally, knew
        that I wanted to leverage the BST structure and use a counter variable.
"""