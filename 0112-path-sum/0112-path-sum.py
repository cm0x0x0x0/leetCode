# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, targetSum, currentSum) -> bool:
            if root.left == None and root.right == None:
                if currentSum + root.val == targetSum:
                    return True
                
                return False
            
            left = False
            right = False
            if root.left != None:
                left = dfs(root.left, targetSum, currentSum + root.val)
            
            if root.right != None:
                right = dfs(root.right, targetSum, currentSum + root.val)
            

            return left or right

            

        if root == None:
            return False

        return dfs(root, targetSum, 0)
        
