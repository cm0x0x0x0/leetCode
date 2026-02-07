class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        table1 = dict()
        table2 = dict()

        for n in nums1:
            if n not in table1:
                table1[n] = 1
            else:        
                table1[n] += 1
        
        for n in nums2:
            if n not in table2:
                table2[n] = 1
            else:
                table2[n] += 1
        
        for k, v in table1.items():
            if k in table2:
                v2 = table2[k]
                minN = min(v, v2)
                result += [k] * minN

        return result
        