class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        table = set()

        if length <= k:
            edgeTable = set(nums)
            return len(edgeTable) != length
            
        for i in range(k+1):
            if nums[i] in table:
                return True
            table.add(nums[i])
        
        for i in range(k+1, length):
            table.remove(nums[i - (k+1)])

            if nums[i] in table:
                return True

            table.add(nums[i])

        return False
            