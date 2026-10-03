class Solution:
    def canJump(self, nums: list[int]) -> bool:
        curIdx = 0
        size = len(nums)
        if size == 1:
            return True

        while curIdx < size:
            delta = 0
            deltaIdx = 0
            for j in range(1, nums[curIdx]+1):
                if curIdx + j >= size-1:
                    return True

                temp = j + nums[curIdx+j]
                if temp > delta:
                    delta = temp
                    deltaIdx = j
            
            curIdx += deltaIdx

            if delta == 0:
                break

        return False