class Solution:
    def verifyGCD(self, base: str, longerStr: str, shorterStr: str) -> bool:
        baseLen = len(base)
        longerLen = len(longerStr)
        shorterLen = len(shorterStr)

        if longerLen % baseLen != 0 or shorterLen % baseLen != 0:
            return False

        shorterIterNum = shorterLen // baseLen
        longerIterNum = longerLen // baseLen

        if base * shorterIterNum != shorterStr:
            return False
        
        if base * longerIterNum != longerStr:
            return False

        return True

        
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        shorterStr = str1 if len(str1) <= len(str2) else str2
        longerStr = str1 if len(str1) > len(str2) else str2

        base = shorterStr
        shorterLen = len(shorterStr)

        for idx in range(shorterLen):
            if self.verifyGCD(base[:shorterLen-idx], longerStr, shorterStr):
                return base[:shorterLen-idx]

        return ""
