class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = 0
        resultNums = []
        hashSet = dict()

        for n in nums:
            if n not in hashSet:
                hashSet[n] = ""
                resultNums.append(n)
                result += 1
        
        nums[:result] = resultNums[:result]

        return result
