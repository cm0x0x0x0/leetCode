from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()

        if root == None:
            return 0

        q.append((root, 1))
        while q:
            node, depth = q.popleft()
            if node.left == None and node.right == None:
                return depth
            
            if node.left != None:
                q.append((node.left, depth+1))
            
            if node.right != None:
                q.append((node.right, depth+1))
        

        return depth
        
