class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = set()
        result = []
        for n in nums1:
            if n not in nums2:
                continue

            if n in table:
                continue
            
            table.add(n)
            result.append(n)
        
        return result
            

