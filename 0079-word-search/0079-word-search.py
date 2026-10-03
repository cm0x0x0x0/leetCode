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

        def dfs(r, c, result):
            result += board[r][c]

            l = len(result)

            if result != word[:l]:
                return False
            
            if result == word:
                print(result, word)
                return True

            for dr, dc in delta:
                newR = r + dr
                newC = c + dc

                if newR < 0 or newR >= rowSize:
                    continue
                
                if newC < 0 or newC >= colSize:
                    continue
                
                if (newR, newC) in visited:
                    continue

                visited.add((newR, newC))
                b = dfs(newR, newC, result)
                if b:
                    return True
                visited.remove((newR, newC))
                
            
            return False

        for i in range(rowSize):
            for j in range(colSize):
                visited.add((i, j))
                b = dfs(i, j, "")
                if b:
                    return True
                visited.remove((i, j))
        
        return False


         