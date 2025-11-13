from collections import deque

class Solution:
    def climbStairs(self, n: int) -> int:
        q = deque()
        s = []
        ways = 0
        q.append(0)
        s.append(0)

        while s:
            # cur = q.popleft()
            cur = s.pop()
            if cur == n:
                ways += 1
                continue

            for step in (2, 1):
                k = cur + step
                if k <= n:
                    # q.append(k)
                    s.append(k)

        return ways