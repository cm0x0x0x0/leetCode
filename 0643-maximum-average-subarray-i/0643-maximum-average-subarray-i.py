class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg = float('-inf')
        tempSum = sum(nums[0:k])
        tempAvg = tempSum / k
        if tempAvg > maxAvg:
            maxAvg = tempAvg

        for startIdx in range(1, len(nums)-k+1):
            tempSum = tempSum - nums[startIdx-1] + nums[startIdx+k-1]
            tempAvg = tempSum / k
            if tempAvg > maxAvg:
                maxAvg = tempAvg

        return maxAvg
        
