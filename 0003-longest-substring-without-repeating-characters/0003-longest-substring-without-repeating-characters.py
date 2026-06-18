class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in table:
                table.remove(s[left])
                left += 1
            
            result = max(result, right-left+1)
            table.add(s[right])

        return result

