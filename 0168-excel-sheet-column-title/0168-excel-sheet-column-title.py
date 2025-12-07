class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        DIVISOR = 26 
        while columnNumber > 0:
            columnNumber -= 1
            k = columnNumber % DIVISOR
            result = chr(65+k) + result
            columnNumber //= DIVISOR

        return result

