class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(startIdx, depth, res):
            if depth == k:
                result.append(res)
                return
            
            for i in range(startIdx, n+1):
                newRes = res[:]
                newRes.append(i)
                dfs(i+1, depth+1, newRes)
        

        dfs(1, 0, [])

        return result