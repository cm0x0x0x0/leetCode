class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        lastIdx = len(nums2)-1

        for n1 in nums1:
            equalFind = False
            addNum = -1
            for idx,n2 in enumerate(nums2):
                if n1 == n2:
                    equalFind = True
                    continue
                
                if not equalFind:
                    continue
                
                if n1 < n2:
                    addNum = n2
                    break
                
            result.append(addNum)
        
        return result


