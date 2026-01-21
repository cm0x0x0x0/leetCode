class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(n, depth, targetDepth, startIdx, res):
            if depth == targetDepth:
                result.append(res)
                return
            
            for i in range(startIdx, n):
                newRes = res[:]
                newRes.append(i)
                dfs(n, depth+1, targetDepth, i+1, newRes)
                
        dfs(n+1, 0, k, 1, [])

        return result