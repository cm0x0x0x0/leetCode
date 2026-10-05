class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        deltas = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]

        visited = set()
        rowSize = len(board)
        colSize = len(board[0])


        def dfs(i, j, region):
            visited.add((i,j))
            region.append((i,j))

            surrounded = not(
                (i == 0 or i == rowSize-1) or
                (j == 0 or j == colSize-1)
            )

            for dr, dc in deltas:
                newR = i + dr
                newC = j + dc

                if newR < 0 or newR >= rowSize:
                    continue
                
                if newC < 0 or newC >= colSize:
                    continue

                if board[newR][newC] == "X":
                    continue
                
                if (newR, newC) in visited:
                    continue
            
                if not dfs(newR, newC, region):
                    surrounded = False
            
            return surrounded
        

        for i in range(rowSize):
            for j in range(colSize):
                if board[i][j] == "O" and (i, j) not in visited:
                    region = []

                    if dfs(i, j, region):
                        for r, c in region:
                            board[r][c] = "X"
            
            

        


        

