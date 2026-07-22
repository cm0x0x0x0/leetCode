import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        k = 0
        r = 0

        if m >= n:
            r = n
        else:
            r = m
        
        #. kCr
        k = m + n - 2
        r -= 1
        result = math.factorial(k) // (math.factorial(k-r) * math.factorial(r))

        return result
        

