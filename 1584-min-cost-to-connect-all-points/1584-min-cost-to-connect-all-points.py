import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def calcManhattan(xi, yi, xj, yj):
            return abs(xi-xj) + abs(yi-yj)

        visited = set()
        n = len(points)
        # (cost, pointIdx)
        heap = [(0, 0)]
        result = 0      

        while len(visited) < n:
            cost, pointIdx = heapq.heappop(heap)

            if pointIdx in visited:
                continue
            
            visited.add(pointIdx)
            result += cost
            xi, yi = points[pointIdx]

            for j in range(n):
                if j in visited:
                    continue
                
                xj, yj = points[j]
                dist = calcManhattan(xi, yi, xj, yj)
                heapq.heappush(heap, (dist, j))
                
        return result


        