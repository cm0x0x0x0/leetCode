class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        st = []
        table = dict()

        for n2 in nums2:
            while st and st[-1] < n2:    
                table[st.pop()] = n2
            st.append(n2)

        for n1 in nums1:
            if n1 not in table:
                result.append(-1)
            else:
                result.append(table[n1])

        return result


