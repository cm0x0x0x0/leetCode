class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        
        # dp[i] = s[:i]까지 word로 채울 수 있나? -> boolean
        dp = [False] * (n+1) # index [0, n]
        dp[0] = True
        
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        
        return dp[n]