class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        rowSize = len(matrix)
        colSize = len(matrix[0])
        top = 0
        bottom = rowSize-1
        left = 0
        right = colSize-1
            
        while top <= bottom and left <= right:
            # 1. col -> right
            for c in range(left, right+1):
                result.append(matrix[top][c])
            top += 1

            # 2. row -> bottom
            if top > bottom:
                break
            for r in range(top, bottom+1):
                result.append(matrix[r][right])
            right -= 1

            # 3. col -> left
            if left > right:
                break
            for c in range(right, left-1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1

            # 4. row -> top
            if top > bottom:
                break
            for r in range(bottom, top-1, -1):
                result.append(matrix[r][left])
            left += 1
            
            
        return result