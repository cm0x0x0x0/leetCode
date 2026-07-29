class Solution:
    def reverse(self, x: int) -> int:
        strX = str(x)

        endIdx = len(strX) - 1
        startIdx = 0
        newStr = ""

        if strX[0] == '-':
            startIdx = 1
            newStr = "-"

        for idx in range(endIdx, startIdx-1, -1):
            newStr += strX[idx]
        
        result = int(newStr)
        if result > 2147483647 or result < -2147483648:
            result = 0

        return result

            