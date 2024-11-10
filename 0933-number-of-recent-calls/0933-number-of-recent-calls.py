class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        startTime = t - 3000

        guessIdx = self.binarySearch(startTime)

        for idx in range(guessIdx, len(self.requests)):
            if self.requests[idx] >= startTime:
                return len(self.requests) - idx
        
        return 0
    
    def binarySearch(self, t:int) -> int: # return: startIdx
        size = len(self.requests)
        halfIdx = size // 2
        while self.requests[halfIdx] > t and halfIdx > 0:
            halfIdx = halfIdx // 2
        
        return halfIdx



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)