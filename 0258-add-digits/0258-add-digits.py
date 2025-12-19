class Solution:
    def addDigits(self, num: int) -> int:
        while num // 10 != 0:
            strNum = str(num)
            length = len(strNum)
            tempSum = 0
            for i in range(length):
                tempSum += int(strNum[i])
            print(tempSum)
            num = tempSum

        return num