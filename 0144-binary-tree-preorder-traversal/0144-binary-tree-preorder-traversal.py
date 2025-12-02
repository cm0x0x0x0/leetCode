# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(root, result) -> List[int]:
            if root == None:
                return result

            result.append(root.val)
            left = preorder(root.left, [])
            right = preorder(root.right, [])
            result += left
            result += right

            return result

    
        
        return preorder(root, [])


