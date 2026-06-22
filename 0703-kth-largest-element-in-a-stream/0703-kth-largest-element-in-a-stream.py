class KthLargest:
    MIN = float("-inf")

    def __init__(self, k, nums):
        self.k = k
        self.nums = sorted(nums, reverse=True)[:k]

        while len(self.nums) < k:
            self.nums.append(self.MIN)

    def add(self, val):
        if val <= self.nums[-1]:
            return self.nums[-1]

        for i in range(self.k):
            if val > self.nums[i]:
                self.nums.insert(i, val)
                self.nums.pop()
                break

        return self.nums[-1]