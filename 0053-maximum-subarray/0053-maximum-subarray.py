class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = float('-inf')
        curSum = float('-inf')

        for i in range(len(nums)):
            curSum = max(curSum+nums[i], nums[i])
            maxSum = max(curSum, maxSum)
            
        return maxSum
