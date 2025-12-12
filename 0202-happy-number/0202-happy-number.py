class Solution:
    def isHappy(self, n: int) -> bool:
        table = set()
        maxNum = (1 << 31) - 1
        target = n

        while target <= maxNum:
            result = 0
            strTarget = str(target)
            for c in strTarget:
                result += pow(int(c), 2)
            
            target = result

            if target in table:
                return False
            table.add(target)

            if target == 1:
                return True
            
        return False

            

        