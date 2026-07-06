class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def isPalindrome(s: str) -> bool:
            l = len(s)
            mid = l // 2 
            for i in range(mid):
                if s[i] != s[l-1-i]:
                    return False
            
            return True
        
        def dfs(s, curList, idx, l):
            nonlocal result
            if idx == l:
                for candidate in curList:
                    if not isPalindrome(candidate):
                        return
                
                result.append(curList)
                return

            
            for j in range(idx+1, l+1):
                dfs(s, curList + [s[idx:j]], j, l)
            
            
        dfs(s, [], 0, len(s))

        return result
