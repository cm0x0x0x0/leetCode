# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTraversal(self, nums: List[int], low, high) -> Optional[TreeNode]:
        if low > high:
            return None
        
        mid = int(((low+high) / 2) + 0.5)
        root = TreeNode(val = nums[mid])
        root.left = self.binaryTraversal(nums, low, mid-1)
        root.right = self.binaryTraversal(nums, mid+1, high)

        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode()
        
        _len = len(nums)
        low = 0
        high = _len - 1
        mid = int(((low+high) / 2) + 0.5)

        root = TreeNode(val=nums[mid])
        root.left = self.binaryTraversal(nums, low, mid-1)
        root.right = self.binaryTraversal(nums, mid+1, high)

        return root