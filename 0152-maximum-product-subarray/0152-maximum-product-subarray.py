class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        prevMax = nums[0]
        prevMin = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]
            prevMaxMulX = prevMax * x
            prevMinMulX = prevMin * x
            curMax = max(x, prevMaxMulX, prevMinMulX)
            curMin = min(x, prevMaxMulX, prevMinMulX)
            prevMax = curMax
            prevMin = curMin
            result = max(result, curMax)
         
        return result