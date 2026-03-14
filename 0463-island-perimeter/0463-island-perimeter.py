class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        delta = [ # (row, col)
            (-1, 0), # up
            (1, 0), # down
            (0, 1), # right
            (0, -1) # left
        ]
        rowSize = len(grid)
        colSize = len(grid[0])

        visited = [[False] * colSize for _ in range(rowSize)]
        st = list()
        perimeter = 0
        
        def isWall(row, col):
            if row < 0 or row == rowSize:
                return True
            
            if col < 0 or col == colSize:
                return True
            
            if grid[row][col] == 0:
                return True
            
            return False

        for i in range(rowSize):
            find = False
            for j in range(colSize):
                if grid[i][j] == 1:
                    st.append((i,j))
                    find = True
                    break
            if find:
                break

        while st:
            i, j = st.pop()
            if visited[i][j]:
                continue

            visited[i][j] = True

            for dr, dc in delta:
                newR = i+dr
                newC = j+dc

                if isWall(newR, newC):
                    perimeter += 1
                    continue
                
                st.append((newR, newC))        

        return perimeter
 