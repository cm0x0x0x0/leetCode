class Solution:
    def firstUniqChar(self, s: str) -> int:
        table = dict()

        for c in s:
            if c not in table:
                table[c] = 1
                continue
            
            table[c] += 1
        
        for idx, c in enumerate(s):
            if table[c] == 1:
                return idx
        
        return -1