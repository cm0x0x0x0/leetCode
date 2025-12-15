class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        table = set()
        for n in nums:
            if n in table:
                return True
            
            table.add(n)
        
        return False