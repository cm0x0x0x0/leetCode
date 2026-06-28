class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        for layer in range(n//2):
            i = layer
            for j in range(i, n-1-i):
                temp = matrix[i][j] # temp <- A
                matrix[i][j] = matrix[n-1-j][i] # A <- D
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j] # D <- C
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i] # C <- B
                matrix[j][n-1-i] = temp # B <- temp(A)



                




