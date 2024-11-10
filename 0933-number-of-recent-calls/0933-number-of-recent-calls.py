class RecentCounter:

    def __init__(self):
        self.requests = collections.deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        startTime = t-3000
        while self.requests[0] < startTime:
            self.requests.popleft()
        
        return len(self.requests)
        



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)