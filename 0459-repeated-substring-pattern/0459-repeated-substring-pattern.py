class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        # substring 길이
        for k in range(1, n // 2 + 1):
            # 길이가 안 나누어 떨어지면 스킵
            if n % k != 0:
                continue

            pattern = s[:k]
            valid = True

            # k 단위로 비교
            for i in range(k, n, k):
                if s[i:i+k] != pattern:
                    valid = False
                    break

            if valid:
                return True

        return False