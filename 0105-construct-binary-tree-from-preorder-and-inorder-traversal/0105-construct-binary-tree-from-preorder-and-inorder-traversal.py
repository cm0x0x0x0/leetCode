# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = 0
        inIdx = {val: idx for idx, val in enumerate(inorder)}

        def dfs(left, right):
            nonlocal preIdx
            if left > right:
                return None

            root = TreeNode(val=preorder[preIdx])
            preIdx += 1

            mid = inIdx[root.val]
            
            # root.left = dfs(preorder[1:i+1], inorder[0:i])
            root.left = dfs(left, mid-1)
            # root.right = dfs(preorder[i+1:], inorder[i+1:])
            root.right = dfs(mid+1, right)

            return root
            

        return dfs(0, len(inorder)-1)