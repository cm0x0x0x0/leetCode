class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = set()
        result = 0
        cur = 0
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] in table:
                    result = max(result, cur)
                    cur = 1
                    table = set()
                    break
                
                cur += 1
                table.add(s[j])
            
            result = max(result, cur)
            cur = 0
        
        return result
