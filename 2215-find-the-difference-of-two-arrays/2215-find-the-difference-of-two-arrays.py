class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = [[],[]]
        appended = {}

        for n in nums1:
            if n not in nums2 and n not in appended:
                result[0].append(n)
                appended[n] = True
        
        for n in nums2:
            if n not in nums1 and n not in appended:
                result[1].append(n)
                appended[n] = True

        return result
        