class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        lenPrices = len(prices)
        maxPriceStart = [0] * lenPrices
        
        maxPriceStart[lenPrices-1] = prices[lenPrices-1]
        for i in range(lenPrices-2, -1, -1):
            if prices[i] > maxPriceStart[i+1]:
                maxPriceStart[i] = prices[i]
                continue
            
            maxPriceStart[i] = maxPriceStart[i+1]

        for i in range(lenPrices-1):
            profit = maxPriceStart[i+1] - prices[i]
            if profit > result:
                result = profit

        return result
                    
                
                
