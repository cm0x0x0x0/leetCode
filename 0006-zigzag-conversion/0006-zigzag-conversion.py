class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        # -- find col number
        numCols = 0
        size = len(s)
        while size > 0:
            numCols += 1 # vertical
            size -= numRows
            if size <= 0:
                break

            delta = numRows - 2
            numCols += min(delta, size)
            size -= delta
        

        # -- make matrix
        matrix = [[""] * numCols for i in range(numRows)]
        size = len(s)
        r = 0
        c = 0
        idx = 0
        while idx < size:
            # vertical
            r = 0
            for i in range(min(numRows, size-idx)):
                matrix[r][c] = s[idx]
                r += 1
                idx += 1

            # diagonal
            r -= 1
            for j in range(min(numRows-2, size-idx)):
                r -= 1
                c += 1
                matrix[r][c] = s[idx]
                idx += 1
            
            c += 1

        
        # -- convert matrix to string
        result = []
        for i in range(numRows):
            for j in range(numCols):
                if matrix[i][j] != "":
                    result.append(matrix[i][j])

        return "".join(result)
