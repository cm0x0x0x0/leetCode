import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = set()

        deltas = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        
        
        while heap:
            t, row, col = heapq.heappop(heap)

            if row == n-1 and col == n-1:
                return t
            
            if (row, col) in visited:
                continue
                
            visited.add((row, col))
            
            for dr, dc in deltas:
                newRow = row + dr
                newCol = col + dc

                if newRow < 0 or newCol < 0 or newRow > n-1 or newCol > n-1:
                    continue
                
                if (newRow, newCol) in visited:
                    continue
                
                newT = max(t, grid[newRow][newCol])
                heapq.heappush(heap, (newT, newRow, newCol))
            
        return -1
        