# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def dfs(node, maxVal):
            nonlocal result
            if node == None:
                return
            
            if node.val >= maxVal:
                result += 1
            
            newMax = max(node.val, maxVal)
            dfs(node.left, newMax)
            dfs(node.right, newMax)
        

        dfs(root, -1*10**4 - 1)

        return result