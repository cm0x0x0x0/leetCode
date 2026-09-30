class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        zeroRows = [False] * m
        zeroCols = [False] * n

        # 0이 있는 행/열 기록
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    zeroRows[r] = True
                    zeroCols[c] = True

        # 기록한 행/열을 0으로 변경
        for r in range(m):
            for c in range(n):
                if zeroRows[r] or zeroCols[c]:
                    matrix[r][c] = 0