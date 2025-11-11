class Solution:
    def mySqrt(self, x: int) -> int:
        for n in range(1, x+1):
            if n*n == x:
                return n
            
            k = n+1
            if n*n < x and k*k >x:
                return n
        
        return 0