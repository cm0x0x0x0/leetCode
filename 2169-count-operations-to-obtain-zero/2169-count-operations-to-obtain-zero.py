class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        counter = 0

        while num1 != 0 and num2 != 0:
            if num1 < num2:
                num2 -= num1
            else:
                num1 -= num2
            
            counter+=1

        return counter