class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        splitList = s.split(' ')

        for subStr in splitList:
            result += ' '
            for c in subStr[::-1]:
                result += c
            
        
        return result[1:]
