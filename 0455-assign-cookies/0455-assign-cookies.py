class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result = 0
        gIdx = 0
        sIdx = 0
        s.sort()
        g.sort()

        while gIdx < len(g) and sIdx < len(s):
            if s[sIdx] >= g[gIdx]:
                result += 1
                gIdx += 1
                sIdx += 1
                continue
            
            if s[sIdx] < g[gIdx]:
                sIdx += 1
                continue
            
            break

        return result
        