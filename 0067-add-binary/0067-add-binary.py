class Solution:
    def binToDec(self, binStr: str) -> int:
        result = 0
        for i, c in enumerate(reversed(binStr)):
            result += pow(2, i) * int(c)

        return result
    
    def decToBin(self, intVal: int) -> str:
        result = ""
        divend = intVal

        while divend > 0:
            mod = int(divend % 2)
            result = str(mod) + result
            divend //= 2
        
        return result if result != "" else "0"

    def addBinary(self, a: str, b: str) -> str:
        decSum = self.binToDec(a) + self.binToDec(b)

        return self.decToBin(decSum)