class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        # memo[(i, j)] : s1의 idx i, s2의 idx j에서 끝까지 만들 수 있는지 여부
        memo = {}

        def dfs(i, j, k):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i == len(s1) and j == len(s2):
                return True
            
            if k >= len(s3):
                return False

            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i+1, j, k+1):
                    memo[(i,j)] = True
                    return True    
            
            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j+1, k+1):
                    memo[(i,j)] = True
                    return True    
            
            memo[(i,j)] = False
            return False
        
        return dfs(0,0,0)
