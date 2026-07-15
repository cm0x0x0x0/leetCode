# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder, inorder):
            if len(preorder) == 0 or len(inorder) == 0:
                return None

            root = TreeNode(val=preorder[0])

            i = 0
            while i < len(inorder):
                if inorder[i] == preorder[0]:
                    break
                    
                i += 1
            
            root.left = dfs(preorder[1:i+1], inorder[0:i])
            root.right = dfs(preorder[i+1:], inorder[i+1:])

            return root
            

        return dfs(preorder, inorder)