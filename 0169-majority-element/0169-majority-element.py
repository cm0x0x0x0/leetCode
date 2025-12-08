class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = 0
        table = dict()
        
        
        threshold = len(nums) / 2
        
        for n in nums:
            if n not in table:
                table[n] = 1
            else:
                table[n] += 1
            
            if table[n] >= threshold:
                return n
        
        return 0
