class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(n):
            if n == 0:
                return 1
            
            half = power(n // 2)

            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
            
        if n < 0:
            return 1 / power(-n)
            
        return power(n)
