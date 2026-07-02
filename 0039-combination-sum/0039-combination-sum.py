class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(substitute, curSum, curCand):
            nonlocal result
            if curSum > target:
                return

            if curSum == target:
                result.append(substitute)
                return

            for cand in candidates:
                if cand < curCand:
                    continue
                newSubs = substitute[:]
                newSubs.append(cand)
                dfs(newSubs, curSum+cand, cand)
            
        dfs([], 0, 0)

        return result