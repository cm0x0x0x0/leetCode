# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def isLeafNode(node: TreeNode) -> bool:
            return node.left == None and node.right == None

        def dfs(node, depth) -> int:
            if isLeafNode(node):
                return depth
            
            leftDepth, rightDepth = 0, 0

            if node.left != None:
                leftDepth = dfs(node.left, depth+1)
            
            if node.right != None:
                rightDepth = dfs(node.right, depth+1)
            
            return max(leftDepth, rightDepth)
        
        if root == None:
            return 0
            
        return dfs(root, 1)
