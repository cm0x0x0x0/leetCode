class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] = word1 앞에서 i글자 -> word2 앞에서 j글자로 변환하는데 필요한 operation수
        memo = {}

        def dp(i, j):
            if i == 0:
                return j
            
            if j == 0:
                return i

            if (i, j) in memo:
                return memo[(i,j)]

            if word1[i-1] == word2[j-1]:
                result = dp(i-1, j-1)
            else:
                result = min(
                    dp(i-1, j-1), # replace
                    dp(i-1, j), # delete
                    dp(i, j-1) # insert
                ) + 1
            
            memo[(i,j)] = result
            return result
        
        return dp(len(word1), len(word2))
