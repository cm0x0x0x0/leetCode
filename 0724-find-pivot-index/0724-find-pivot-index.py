class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        def getSum(nums: List[int]) -> int:
            return sum(nums)

        size = len(nums)
        for idx in range(size):
            leftSum = getSum(nums[:idx])
            rightSum = getSum(nums[idx+1:])
            if leftSum == rightSum:
                return idx
        
        return -1
        


            