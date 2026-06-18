class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        
        for i in range(len(s)):
            table = set()
            for j in range(i, len(s)):
                if s[j] in table:
                    break
                
                table.add(s[j])
                result = max(result, j-i+1)
        
        return result
