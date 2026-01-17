# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        result = 1
        start = 1
        end = n
        mid = (start+end) // 2

        while start <= end:
            if not isBadVersion(mid):
                start = mid+1
                mid = (start+end) // 2
                continue
            
            result = mid
            end = mid-1
            mid = (start+end) // 2

        return result