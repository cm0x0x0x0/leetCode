class Solution:
    def isUgly(self, n: int) -> bool:
        dividends = [2,3,5]
        
        def dfs(n):
            if n == 1:
                return True
            
            for d in dividends:
                if n % d ==0:
                    if dfs(n//d):
                        return True
                        
            return False
        
        return dfs(n)
        
        