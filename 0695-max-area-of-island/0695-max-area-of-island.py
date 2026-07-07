class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        visited = dict()
        rowSize = len(grid)
        colSize = len(grid[0])

        delta = [
            # row, col
            [0, 1], # east
            [0, -1], # west
            [1, 0], # south
            [-1, 0] # north
        ]

        def isOut(row, col):
            if row < 0 or col < 0:
                return True
            
            if row >= rowSize or col >= colSize:
                return True

            return False

        def dfs(row, col):
            nonlocal result
            if (row,col) in visited:
                return 0
            
            if grid[row][col] == 0:
                return 0

            visited[(row,col)] = True

            area = 1
            for dr, dc in delta:
                newRow = row + dr
                newCol = col + dc

                if isOut(newRow, newCol):
                    continue
                
                area += dfs(newRow, newCol)
            
            return area

        for row in range(rowSize):
            for col in range(colSize):
                if (row, col) in visited:
                    continue
                
                area = dfs(row, col)
                if area > result:
                    result = area

        return result

