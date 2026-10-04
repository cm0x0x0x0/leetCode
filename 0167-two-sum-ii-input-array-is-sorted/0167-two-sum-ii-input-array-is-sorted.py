class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        
        def binarySearch(num, left, right):
            while left <= right:
                mid = (left+right) // 2

                if numbers[mid] == num:
                    return mid
                elif numbers[mid] > num:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return -1

        for i in range(n):
            j = binarySearch(target-numbers[i], i+1, n-1)
            if j != -1:
                return [i+1, j+1]
        
        return [0,0]

