class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        def setToZero(row, col):
            for r in range(m):
                matrix[r][col] = 0

            for c in range(n):
                matrix[row][c] = 0
            
        zeroRowCols = []
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    zeroRowCols.append((r,c))
        
        for r,c in zeroRowCols:
            setToZero(r,c)
        