# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, left, right) -> bool:
        if left == None and right == None:
            return True
        
        if left == None or right == None:
            return False
        
        if left.val != right.val:
            return False

        return self.isSameTree(left.left, right.right) and self.isSameTree(left.right, right.left)
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSameTree(root.left, root.right)