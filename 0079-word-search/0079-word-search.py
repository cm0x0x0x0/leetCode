class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rowSize = len(board)
        colSize = len(board[0])
        visited = set()

        delta = [
            # (row, col)
            (-1, 0), # north
            (0, 1), # east
            (1, 0), # south
            (0, -1) # west
        ]


        def dfs(r, c, idx):
            if r < 0 or r >= rowSize or c < 0 or c >= colSize:
                return False

            if (r, c) in visited:
                return False

            if board[r][c] != word[idx]:
                return False

            if idx == len(word) - 1:
                return True

            visited.add((r, c))

            for dr, dc in delta:
                if dfs(r + dr, c + dc, idx + 1):
                    return True

            visited.remove((r, c))

            return False

        for i in range(rowSize):
            for j in range(colSize):
                b = dfs(i, j, 0)
                if b:
                    return True
        
        return False


         