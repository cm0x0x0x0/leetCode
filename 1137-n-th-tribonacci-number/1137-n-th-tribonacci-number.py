class Solution:
    result = dict()

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
            
        if n in Solution.result:
            return Solution.result[n]

        temp = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
        if temp not in Solution.result:
            Solution.result[n] = temp
        
        return Solution.result[n]