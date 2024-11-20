class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = [1] * size
        
        # prefix
        curMul = 1
        for i in range(1,size):
            curMul *= nums[i-1]
            result[i] *= curMul
        
        # suffix
        curMul = 1
        for i in range(size-2, -1, -1):
            curMul *= nums[i+1]
            result[i] *= curMul

        return result
            