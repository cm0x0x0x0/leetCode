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
            nonlocal result

            while not isOut(left, right) and s[left] == s[right]:
                if right-left+1 > len(result):
                    result = s[left:right+1]

                left -= 1
                right += 1
                

        for i in range(size):
            find(i, i) # odd
            find(i, i+1) # even

        return result