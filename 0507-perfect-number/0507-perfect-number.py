class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        curSum = 1
        for n in range(2, int(num**0.5)+1):
             if num % n == 0:
                curSum += n

                other = num // n
                if other != n:
                    curSum += other

                if curSum > num:
                    return False
        
        return curSum == num