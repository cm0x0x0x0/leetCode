class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        result = 0
        table = set(nums)

        for n in table:
            if n-1 in table:
                continue
            
            # start point
            cur = n
            count = 0
            while cur in table:
                count += 1
                cur += 1
            
            if count > result:
                result = count
            
        return result


