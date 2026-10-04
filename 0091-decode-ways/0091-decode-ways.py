class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}

        def dfs(idx):
            if idx == n:
                return 1
            
            if s[idx] == '0':
                return 0
            
            if idx in memo:
                return memo[idx]
            
            # 1-digit case
            count = dfs(idx+1)

            # 2-digit case
            if idx + 1 < n and (
                s[idx] == '1' or (s[idx] == '2' and s[idx+1] <= '6')
            ):
                count += dfs(idx+2)
            
            memo[idx] = count

            return count
        
        return dfs(0)