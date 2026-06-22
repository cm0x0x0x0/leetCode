import heapq

class KthLargest:
    MIN = float("-inf")

    def __init__(self, k, nums):
        self.k = k
        self.nums = sorted(nums, reverse=True)[:k]
        heapq.heapify(self.nums)

    def add(self, val):
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heappush(self.nums, val)
            heapq.heappop(self.nums)
    

        return self.nums[0] if len(self.nums) == self.k else 0