class Solution:
    def hammingWeight(self, n: int) -> int:
        def dec2bin(n: int) -> str:
            result = ""
            while n > 0:
                result = str(n%2) + result
                n //= 2

            return result

        binNum = dec2bin(n)
        count = 0
        for c in binNum:
            if c == "1":
                count += 1
        
        return count