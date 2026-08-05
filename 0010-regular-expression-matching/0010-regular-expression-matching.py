class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sLen = len(s)
        pLen = len(p)

        cache = dict()

        def dfs(sIdx, pIdx):
            if (sIdx, pIdx) in cache:
                return cache[(sIdx, pIdx)]

            if sIdx == sLen and pIdx == pLen:
                cache[(sIdx, pIdx)] = True
                return True
            
            if pIdx >= pLen:
                cache[(sIdx, pIdx)] = False
                return False

            firstMatch = (
                sIdx < sLen and
                (p[pIdx] == s[sIdx] or p[pIdx] == '.')
            )
            
            if pIdx+1 < pLen and p[pIdx+1] == '*':
                result = dfs(sIdx, pIdx+2) or (firstMatch and dfs(sIdx+1, pIdx))
                cache[(sIdx, pIdx)] = result
                return result

            result = firstMatch and dfs(sIdx+1, pIdx+1)
            cache[(sIdx, pIdx)] = result
            return result

        return dfs(0,0)

