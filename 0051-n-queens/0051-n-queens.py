class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        delta = [
            (1, 0),
            (-1, 0),
            (1, 1),
            (-1, -1),
            (-1, 1),
            (1, -1)
        ]
        visited = [[-1] * n for _ in range(n)]

        def setVisited(row, col):
            if visited[row][col] == -1:
                visited[row][col] = row

            for dr, dc in delta:
                newRow = row + dr
                newCol = col + dc

                while 0 <= newRow < n and 0 <= newCol < n:
                    if visited[newRow][newCol] == -1:
                        visited[newRow][newCol] = row
                    newRow += dr
                    newCol += dc
        
        def unsetVisited(row, col):
            if visited[row][col] == row:
                visited[row][col] = -1

            for dr, dc in delta:
                newRow = row + dr
                newCol = col + dc

                while 0 <= newRow < n and 0 <= newCol < n:
                    if visited[newRow][newCol] == row:
                        visited[newRow][newCol] = -1
                    newRow += dr
                    newCol += dc        

        def isValid(row, col):
            return visited[row][col] == -1

        def dfs(row, matrixResult):
            if row == n:
                result.append(matrixResult)
                return

            for col in range(n):
                if not isValid(row, col):
                    continue
                
                rowResult = "." * col
                rowResult = rowResult + "Q"
                rowResult = rowResult + "." * (n-col-1)

                setVisited(row, col)
                temp = matrixResult[:]
                temp.append(rowResult)
                dfs(row+1, temp)
                unsetVisited(row,col)

        dfs(0, [])

        return result
        