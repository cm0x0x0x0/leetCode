class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        MIN = (-1) * (2**31) - 1
        duple = set()
        first = MIN
        second = MIN
        third = MIN

        for n in nums:
            if n in duple:
                continue

            if n > first:
                third = second
                second = first
                first = n
            elif n > second:
                third = second
                second = n
            elif n > third:
                third = n
            
            duple.add(n)

        if third == MIN:
            return first
        
        return third


