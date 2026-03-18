class Solution:
    def countSegments(self, s: str) -> int:
        result = 0
        for c in s.split(' '):
            if c == "":
                continue
            result += 1
        
        return result