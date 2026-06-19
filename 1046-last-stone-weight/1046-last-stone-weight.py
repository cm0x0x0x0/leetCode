import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def smash(x, y):
            if x > y:
                temp = y
                y = x
                x = temp
            
            return y - x

        hq = []    

        for st in stones:
            heapq.heappush(hq, -st)

        while len(hq) > 1:
            x = heapq.heappop(hq)
            y = heapq.heappop(hq)
            k = smash(x,y)

            heapq.heappush(hq, -k)

        return hq[0] * (-1)



