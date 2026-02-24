class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        table = dict()

        for c in s:
            if c not in table:
                table[c] = 1
            else:
                table[c] += 1
        
        for c in t:
            if c not in table:
                return c
            
            if table[c] == 0:
                return c
            
            table[c] -= 1
        
        return ""