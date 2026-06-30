# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = -1
        cnt = 0

        def dfs(node):
            nonlocal cnt, result

            if not node or result != -1:
                return
            
            dfs(node.left)

            cnt += 1
            if cnt == k:
                result = node.val
                return
            
            dfs(node.right)
            
        dfs(root)
        return result