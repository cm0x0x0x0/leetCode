import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        result = []
        heap = []

        for x, y in points:
            dist = (x*x + y*y) # intentionally no root
            heap.append((dist, [x,y]))
        
        heapq.heapify(heap)
        
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result
