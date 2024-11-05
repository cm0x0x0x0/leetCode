class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        size = len(strX)
        half = size // 2
        
        for i in range(half):
            if strX[i] != strX[size-1-i]:
                return False
            
        return True
        
        