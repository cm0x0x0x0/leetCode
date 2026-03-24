class Solution:
    def toLowerCase(self, s: str) -> str:
        def toLowerChar(c: str) -> str:
            if c >= 'A' and c <= 'Z':
                return chr(ord(c)+32)
            
            return c
        
        return "".join([toLowerChar(c) for c in s])