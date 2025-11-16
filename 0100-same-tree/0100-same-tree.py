# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, p, q) -> bool:
        if p == None and q == None:
            return True
        
        if p == None or q == None:
            return False

        if self.inorder(p.left, q.left) == False:
            return False
        
        if p.val != q.val:
            return False
        
        if self.inorder(p.right, q.right) == False:
            return False

        return True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.inorder(p, q)
        