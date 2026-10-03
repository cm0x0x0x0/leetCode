class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = []
        result.append([])
        size = len(nums)
        nums.sort()

        def dfs(idx, curResult):
            if curResult not in result:
                result.append(curResult[:])
            
            for i in range(idx+1, size):
                curResult.append(nums[i])
                dfs(i, curResult)
                curResult.pop()
            
        for i in range(size):
            dfs(i, [nums[i]])

        return result