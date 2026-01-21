class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        subResult = []

        def dfs(startIdx):
            if len(subResult) == k:
                result.append(subResult[:])
                return
            
            for i in range(startIdx, n+1):
                subResult.append(i)
                dfs(i+1)
                subResult.pop()
        
        dfs(1)

        return result