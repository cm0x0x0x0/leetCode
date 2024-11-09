class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)

        nonZeros = []

        for idx in range(size):
            if nums[idx] != 0:
                nonZeros.append(nums[idx])

        for idx in range(len(nonZeros)):
            nums[idx] = nonZeros[idx]
        
        for idx in range(len(nonZeros), size):
            nums[idx] = 0
