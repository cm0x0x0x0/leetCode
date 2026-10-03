class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = float('-inf')
        curSum = float('-inf')
        startIdx = 0

        for i in range(len(nums)):
            if curSum+nums[i] <= nums[i]:
                startIdx = i
                curSum = nums[i]
            else:
                curSum += nums[i]
            
            if curSum > maxSum:
                maxSum = curSum
            
        return maxSum
