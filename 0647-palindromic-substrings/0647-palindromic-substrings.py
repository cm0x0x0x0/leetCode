class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        n = len(s)

        def expand(left, right):
            count = 0

            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            
            return count

        for i in range(n):
            result += expand(i, i)   # odd
            result += expand(i, i+1) # even

        return result