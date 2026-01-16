class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        pairCount = 0
        maxSingleCount = 0
        maxSingleKey = None
        table = dict()
        for c in s:
            if c not in table:
                table[c] = 1
                continue
            
            table[c] += 1
        
        for k,v in table.items():
            if v & 1:
                if v > maxSingleCount:
                    maxSingleKey = k
                    maxSingleCount = v
                continue
            
            pairCount += v
        
        result += pairCount
        for k, v in table.items():
            if (v & 1) == 0:
                continue
            
            if k == maxSingleKey:
                result += table[k]
                continue
            
            result += table[k]-1

        return result


            
