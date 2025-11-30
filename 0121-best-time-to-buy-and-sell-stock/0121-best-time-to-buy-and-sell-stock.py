class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [0] * len(prices)
        lenPrices = len(prices)

        for i in range(lenPrices-1):
            for j in range(i+1, lenPrices):
                if prices[j] <= prices[i]:
                    continue

                profit = prices[j] - prices[i]
                if profit > profits[i]:
                    profits[i] = profit
        

        return max(profits)
                    
                
                
