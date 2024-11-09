class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = [[],[]]
        appended = {}

        nums1Set = set(nums1)
        nums2Set = set(nums2)

        def findUniqueNums(targetList, compareSet):
            result = []
            for n in targetList:
                if n not in compareSet and n not in appended:
                    result.append(n)
                    appended[n] = True    
            
            return result

        result[0] = findUniqueNums(nums1, nums2Set)
        result[1] = findUniqueNums(nums2, nums1Set)

        return result
        