class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        
        result = s[0]
        resultLen = 1

        def isOut(left, right):
            if left < 0 or right < 0:
                return True
            
            if left >= size or right >= size:
                return True
            

            return False
        

        def find(left, right):
            nonlocal result, resultLen
            if s[left] != s[right]:
                return

            if s[left] == s[right] and resultLen < (right-left+1):
                result = s[left:right+1]
                resultLen = right-left+1
            
            newLeft = left-1
            newRight = right + 1
            if not isOut(newLeft, newRight):
                find(newLeft, newRight)
                
        
        # odd
        for i in range(1, size-1):
            left = i
            right = i
            if not isOut(left, right):
                find(left, right)
        

        # even
        for i in range(0, size-1):
            left = i
            right = i+1
            if not isOut(left, right):
                find(left, right)

        return result