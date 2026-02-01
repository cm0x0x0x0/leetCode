# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        def dfs(root, subResult):
            subResult.append(str(root.val))
            if root.left == None and root.right == None:
                result.append("->".join(subResult))
                return
            
            if root.left != None:
                dfs(root.left, subResult[:])    
            
            if root.right != None:
                dfs(root.right, subResult[:])
        
        dfs(root, [])

        return result
