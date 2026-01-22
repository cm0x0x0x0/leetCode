class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        k = len(nums)
        visited = [False] * k
        unique = set()

        def dfs(res):
            if len(res) == k:
                t = tuple(res)
                if t not in unique:
                    unique.add(t)
                    result.append(res)
                return

            for i in range(k):
                if visited[i]:
                    continue
                
                visited[i] = True
                newRes = res[:]
                newRes.append(nums[i])
                dfs(newRes)
                visited[i] = False
        

        dfs([])

        return result


