class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []

        idx1 = 0 
        idx2 = 0
        len1 = len(nums1)
        len2 = len(nums2)


        # sorting O(m+n)
        while idx1 < len1 and idx2 < len2:
            if nums1[idx1] <= nums2[idx2]:
                nums3.append(nums1[idx1])
                idx1 += 1
                continue
            
            nums3.append(nums2[idx2])
            idx2 += 1


        while idx1 < len1:
            nums3.append(nums1[idx1])
            idx1 += 1
        

        while idx2 < len2:
            nums3.append(nums2[idx2])
            idx2 += 1

        len3 = len1+len2
        isOdd = len3 & 1
        median = 0

        if isOdd:
            i = len3 // 2
            median = nums3[i]
        else:
            i = len3 // 2
            median = (nums3[i-1] + nums3[i])/2

        return median