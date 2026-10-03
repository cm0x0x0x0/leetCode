class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = []
        size = len(nums)
        nums.sort()

        def dfs(idx, curResult):
            result.append(curResult[:])
            
            for i in range(idx, size):
                if i > idx and nums[i] == nums[i - 1]:
                    continue

                curResult.append(nums[i])
                dfs(i+1, curResult)
                curResult.pop()
            
        dfs(0, [])

        return result