class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prefix = [1] * size
        suffix = [1] * size

        curMul = 1
        for i in range(1,size):
            curMul *= nums[i-1]
            prefix[i] = curMul
        
        curMul = 1
        for i in range(size-2, -1, -1):
            curMul *= nums[i+1]
            suffix[i] = curMul
        
        result = [prefix[i]*suffix[i] for i in range(size)]

        return result
            