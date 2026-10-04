class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        m = len(grid) # row
        n = len(grid[0]) # col
        deltas = [
            (-1, 0), # north
            (0, 1), # east
            (1, 0), # south
            (0, -1)  # west
        ]

        visited = set()

        def dfs(row, col):
            if row < 0 or row >= m:
                return
            
            if col < 0 or col >= n:
                return

            if (row, col) in visited:
                return

            if grid[row][col] == "0":
                return
            
            visited.add((row, col))
            for dr, dc in deltas:
                dfs(row+dr, col+dc)        


        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    result += 1

        return result




