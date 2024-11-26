from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        depthCheck = dict()
        queue = deque()
        if root == None:
            return result
        
        queue.append((root, 0))
        
        while len(queue) > 0:
            node, depth = queue.popleft()
            if depth not in depthCheck:
                depthCheck[depth] = True
                result.append(node.val)

            if node.right != None:
                queue.append((node.right, depth+1))
            
            if node.left != None:
                queue.append((node.left, depth+1))
        
        return result


            


        