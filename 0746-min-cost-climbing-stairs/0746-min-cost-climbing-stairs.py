class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost)
        dp = [float('inf') for _ in range(size)]
        
        dp[size-1] = cost[size-1]
        dp[size-2] = cost[size-2]

        for idx in range(len(cost)-3, -1, -1):
            curCost1 = cost[idx] + dp[idx+1]
            curCost2 = cost[idx] + dp[idx+2]
            dp[idx] = min(curCost1, curCost2)
        
        return min(dp[0], dp[1])
