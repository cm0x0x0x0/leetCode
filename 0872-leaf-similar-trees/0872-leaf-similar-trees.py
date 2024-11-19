# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, result):
            val = root.val
            
            if root.left == None and root.right == None:
                result.append(val)
            
            if root.left != None:
                dfs(root.left, result)

            if root.right != None:
                dfs(root.right, result)    

        r1, r2 = [], []
        dfs(root1, r1)
        dfs(root2, r2)

        return r1 == r2
