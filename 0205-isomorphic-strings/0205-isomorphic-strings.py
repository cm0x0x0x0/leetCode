class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        table = dict()
        table2 = dict()
        length = len(s)

        newT = ""
        for idx in range(length):
            if s[idx] in table:
                if table[s[idx]] != t[idx]:
                    return False

            if t[idx] in table2:
                if table2[t[idx]] != s[idx]:
                    return False

            table[s[idx]] = t[idx]
            table2[t[idx]] = s[idx]
            newT += table[s[idx]]
        
        return t == newT
        
        

        
            
