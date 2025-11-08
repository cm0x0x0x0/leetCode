class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        maxLen = len(nums)
        low = 0
        high = len(nums)-1
        mid = int((low+high)/2)

        while True:
            print(low, mid, high)
            if nums[mid] == target:
                return mid
                
            if low+1 >= high:
                if target > nums[high]:
                    return high + 1
                elif target < nums[low]:
                    return low

                return high
            
            if nums[mid] > target:
                high = mid
                mid = int((low+high)/2)
                continue
            
            low = mid
            mid = int((low+high)/2)

        return -1