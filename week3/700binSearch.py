# Initial implementation of binary search 
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root
        
        if val < root.val:
            newRoot = root.left
        else:
            newRoot = root.right
        return self.searchBST(newRoot, val)