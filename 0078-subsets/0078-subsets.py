class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        visited = set()
        candidates = nums
        size = len(candidates)

        def dfs(idx, cur):
            result.append(cur[:])

            for j in range(idx+1, size):
                temp = cur[:]
                temp.append(candidates[j])    
                dfs(j, temp[:])
                
            return
        
        for i in range(size):
            dfs(i, [candidates[i]])
            
        return result
        