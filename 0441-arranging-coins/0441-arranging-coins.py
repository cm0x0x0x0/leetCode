class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
            
        for i in range(1, n+1):
            si = i*(i+1) / 2
            if si > n:
                return i-1
        
        return 0