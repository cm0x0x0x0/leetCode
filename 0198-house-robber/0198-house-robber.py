class Solution:
    def rob(self, nums: list[int]) -> int:
        size = len(nums)
        if size == 1:
            return nums[0]

        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for k in range(2, size):
            dp[k] = max(dp[k-2]+nums[k], dp[k-1])

        return dp[size-1]
