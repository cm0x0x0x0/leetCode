class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(cur, leftCnt, rightCnt):
            if leftCnt == n and rightCnt == n:
                result.append(cur)
                return
            
            if rightCnt > leftCnt:
                return
            
            if leftCnt < n:
                dfs(cur+"(", leftCnt+1, rightCnt)
            
            if rightCnt < n:
                dfs(cur+")", leftCnt, rightCnt+1)
            

        dfs("", 0, 0)

        return result