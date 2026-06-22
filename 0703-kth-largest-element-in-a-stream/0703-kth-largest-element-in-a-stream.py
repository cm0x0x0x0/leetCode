class KthLargest:
    minNum = -10**4

    def __init__(self, k: int, nums: List[int]):
        temp = sorted(nums, reverse=True)
        self.k = k
        self.nums = temp[:k]
        self.nums += [self.minNum] * (self.k - len(self.nums))
        

    def add(self, val: int) -> int:
        if val <= self.nums[self.k-1]:
            return self.nums[self.k-1]
        
        newArr = [0] * self.k
        idx = 0
        while idx < len(self.nums):
            if val > self.nums[idx]:
                newArr[idx] = val
                newArr[idx+1:self.k] = self.nums[idx:self.k-1]
                break
            
            newArr[idx] = self.nums[idx]
            idx += 1
        
        self.nums = newArr
        result = self.nums[self.k-1]
        return result if result >= self.minNum else 0

        



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)