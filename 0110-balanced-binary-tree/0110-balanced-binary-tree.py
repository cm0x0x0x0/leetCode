# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root) -> (bool, int): # (isBalanced, height)
        if root == None:
            return (True, 0)

        balanced1, height1 = self.dfs(root.left)
        balanced2, height2 = self.dfs(root.right)

        isBalanced = (balanced1 and balanced2) and abs(height1-height2) <= 1

        return (isBalanced, 1 + max(height1, height2))


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]