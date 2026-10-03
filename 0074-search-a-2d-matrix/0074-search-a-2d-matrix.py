class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # row search
        rowSize = len(matrix)
        left = 0
        right = rowSize-1
        mid = (left+right) // 2

        while left < right:
            if matrix[mid][0] <= target and target < matrix[mid+1][0]:
                break
            
            if target > matrix[mid][0]:
                left = mid+1
            else:
                right = mid-1
            
            mid = (left+right) // 2
        
        row = mid
        
        # col search
        colSize = len(matrix[0])
        left = 0
        right = colSize-1
        mid = (left+right) // 2

        while left <= right:
            if matrix[row][mid] == target:
                return True
            
            if target > matrix[row][mid]:
                left = mid+1
            else:
                right = mid-1
            
            mid = (left+right) // 2

        return False