class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(c for c in s if c >= 'a' and c <= 'z')

        _len = len(s)
        mid = _len // 2

        if _len == 1:
            return False

        for i in range(mid):
            if s[i] != s[_len-1-i]:
                return False
        
        return True
