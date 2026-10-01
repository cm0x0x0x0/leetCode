# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def binarySearch(root, target):
            result = []
            node = root

            while node.val != target:
                result.append(node)

                if node.val > target:
                    node = node.left
                else:
                    node = node.right
            
            result.append(node)
                        
            return result
        
        firstList = binarySearch(root, p.val)
        secondList = binarySearch(root, q.val)
        # firstValList = [x.val for x in firstList]
        compSet = set(firstList)
    
        for n in reversed(secondList):
            if n in compSet:
                return n
        
        return TreeNode()