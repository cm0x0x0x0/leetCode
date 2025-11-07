class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystackLen = len(haystack)
        needleLen = len(needle)
        
        if haystack == needle:
            return 0
                        
        for i in range(haystackLen - needleLen+1):
            if haystack[i:i+needleLen] == needle:
                return i
        
        return -1