from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q = deque()
        rowSize = len(grid)
        colSize = len(grid[0])

        freshCellCount = 0
        for r in range(rowSize):
            for c in range(colSize):
                if grid[r][c] == 1:
                    freshCellCount += 1

                if grid[r][c] == 2:
                    q.append((r,c,0))
                    
        if freshCellCount == 0:
            return 0
        
        deltas = [
            (0, 1),  # right
            (1, 0),  # down
            (-1, 0), # up
            (0, -1)  # left
        ]

        visited = set()
        result = 0
        while q:
            r, c, turn = q.popleft()
            if (r,c) in visited:
                continue
                
            visited.add((r,c))
            if grid[r][c] == 1:
                grid[r][c] = 2
                freshCellCount -= 1

            if turn > result:
                result = turn

            for dr, dc in deltas:
                newR = r+dr
                newC = c+dc

                if newR < 0 or newR >= rowSize:
                    continue
                
                if newC < 0 or newC >= colSize:
                    continue

                if grid[newR][newC] == 0:
                    continue
                
                q.append((newR, newC, turn+1))
        
    
        return result if freshCellCount == 0 else -1
        

                

                

                

                
                

