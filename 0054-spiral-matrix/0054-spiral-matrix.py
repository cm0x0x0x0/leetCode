class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        rowSize = len(matrix)
        colSize = len(matrix[0])
        totalCount = rowSize * colSize
        visited = set()

        rowIdx = 0
        colIdx = 0

        def move(row, col):
            nonlocal rowIdx, colIdx
            # False : exit
            if (row, col) in visited:
                return False
            
            visited.add((row,col))
            result.append(matrix[row][col])
            rowIdx = row
            colIdx = col
            
        while len(visited) < totalCount:
            # 1. col -> colEnd
            for c in range(colSize):
                exit = move(rowIdx, c)
                if exit:
                    break

            # 2. row -> rowEnd
            for r in range(rowSize):
                exit = move(r, colIdx)
                if exit:
                    break

            # 3. col -> 0
            for c in range(colIdx-1, -1, -1):
                exit = move(rowIdx, c)
                if exit:
                    break

            # 4. row -> 0
            for r in range(rowIdx-1, -1, -1):
                exit = move(r, colIdx)
                if exit:
                    break
            
        return result