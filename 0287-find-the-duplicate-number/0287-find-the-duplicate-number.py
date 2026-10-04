class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # a : 사이클 시작지점 -> 사이클 입구 거리
        # b : 사이클 입구 -> 처음 만난지점 거리
        # L : 사이클 1바퀴 거리
        # slow : t 만큼 이동
        # fast : 2t 만큼 이동
        # 2t - t = kL
        # t = kL
        # t = a + b + mL (slow 이동거리)
        # a+b = (k-m)L

        slow = 0
        fast = 0
        count = 0

        # 1. find join point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        # 2. find cycle entrace
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow