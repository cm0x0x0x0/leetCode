class Solution:
    def jump(self, nums: list[int]) -> int:
        i = 0
        result = 0
        target = len(nums) - 1

        while i < target:
            if i + nums[i] >= target:
                result += 1
                break

            maxReach = -1
            nextIdx = -1
            # 현재에서 갈 수 있는 범위 
            for j in range(i + 1, i + nums[i] + 1):
                candidateIdx = j + nums[j]
                if candidateIdx > maxReach:
                    maxReach = candidateIdx
                    nextIdx = j

            i = nextIdx
            result += 1

        return result