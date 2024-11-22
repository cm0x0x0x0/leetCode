class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        length = len(nums)
        minNum = float('inf')
        maxNum = float('-inf')

        minFirstToIdx = [maxNum] * length
        maxIdxToLast = [minNum] * length

        if length < 3:
            return False

        for i in range(length):
            # upward
            if minNum > nums[i]:
                minNum = nums[i]
            minFirstToIdx[i] = minNum

            # downward
            if maxNum < nums[length-1-i]:
                maxNum = nums[length-1-i]
            maxIdxToLast[length-1-i] = maxNum
        
        for i in range(length):
            if nums[i] > minFirstToIdx[i] and nums[i] < maxIdxToLast[i]:
                return True

        return False
