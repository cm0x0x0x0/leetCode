class Solution:
    def countBits(self, n: int) -> List[int]:
        def countBit(n):
            result = 0
            pivot = 1
            while pivot <= n:
                if n & pivot == pivot:
                    result += 1
                pivot = pivot << 1
            
            return result

        
        result = []
        for i in range(n+1):
            result.append(countBit(i))
        
        return result