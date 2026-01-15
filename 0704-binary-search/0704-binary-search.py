class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        start = 0
        end = length-1
        half = length // 2
    
        while half < end:
            if nums[half] == target:
                return half
            
            if nums[half] > target:
                end = half-1
                half = (start+end)//2
                continue
            
            start = half+1
            half = (start+end)//2
        
        return -1


