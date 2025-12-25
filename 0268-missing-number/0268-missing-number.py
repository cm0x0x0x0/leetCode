class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxNum = len(nums)
        table = dict()
        for n in nums:
            table[n] = True
        
        for i in range(0, maxNum+1):
            if i not in table:
                return i
        
        return 0


        