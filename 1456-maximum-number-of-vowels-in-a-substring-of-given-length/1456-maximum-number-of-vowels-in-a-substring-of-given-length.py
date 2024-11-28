class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        temp = 0
        result = 0
        lowers = ['a', 'e', 'i', 'o', 'u']
        
        length = len(s)
        subString = s[:k]
        
        for c in subString:
            if c in lowers:
                result += 1

        temp = result
        for i in range(k, length):
            if subString[0] in lowers:
                temp -= 1
            
            if s[i] in lowers:
                temp += 1

            subString = subString[1:k] + s[i]
            if temp > result:
                result = temp
            
        return result 
        
        