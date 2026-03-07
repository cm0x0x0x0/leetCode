class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1 == "0" and num2 == "0":
            return "0"
        
        result = ""
        temp = 0
        strToInt = dict()
        intToStr = dict()
        for n in range(0, 10):
            strToInt[str(n)] = n
            intToStr[n] = str(n)

        if len(num1) < len(num2):
            tempArr = num2[:]
            num2 = num1[:]
            num1 = tempArr[:]
        
        # num1Len >= num2Len
        num1Len = len(num1)
        num2Len = len(num2)

        def processCarry():
            nonlocal temp, result
            if temp >= 10:
                k = temp % 10
                result = intToStr[k] + result
                temp = temp // 10
            else:
                result = intToStr[temp] + result
                temp = 0


        for idx in range(num2Len):
            temp += strToInt[num1[num1Len-idx-1]]
            temp += strToInt[num2[num2Len-idx-1]]
            processCarry()
        
        diff = num1Len - num2Len
        for idx in range(diff):
            temp += strToInt[num1[diff-idx-1]]
            processCarry()
        
        if temp > 0:
            processCarry()
            
        return result

            


        
