# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = -1
        arr = []
        cnt = 0
        find = False

        def dfs(node):
            nonlocal cnt, result, arr
            if node.left == None and node.right == None:
                arr.append(node.val)
                cnt += 1
                if cnt == k:
                    result = node.val
                return
                
            if node.left != None:
                dfs(node.left)
                if cnt == k:
                    return

            arr.append(node.val)
            cnt += 1
            if cnt == k:
                result = node.val
                return

            if node.right != None:
                dfs(node.right)
            

        dfs(root)
        return root.val if result == -1 else result