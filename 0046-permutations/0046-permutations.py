class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        k = len(nums)

        def dfs(res, visited: List[bool]):
            if len(res) == k:
                result.append(res)
                return
            
            for idx, n in enumerate(nums):
                if visited[idx]:
                    continue

                visited[idx] = True
                newRes = res[:]
                newRes.append(n)
                dfs(newRes, visited[:])
                visited[idx] = False
            
        dfs([], [0]*k)

        return result