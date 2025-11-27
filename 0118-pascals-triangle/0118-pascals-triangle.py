class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals = [[1], [1,1]]
        
        for i in range(2, numRows):
            newList = [1]
            for j in range(i-1):
                newList.append(pascals[i-1][j] + pascals[i-1][j+1])
            newList.append(1)
            pascals.append(newList)

            
        return pascals[:numRows]


