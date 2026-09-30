class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        size = len(candidates)

        def findTargetSum(curIdx, curSum, curList):
            if curSum > target:
                return

            if curSum == target:
                result.append(curList.copy())
                return
                
            for i in range(curIdx, size):
                if i > curIdx and candidates[i] == candidates[i-1]:
                    continue
                
                if curSum+candidates[i] > target:
                    break

                curList.append(candidates[i])
                findTargetSum(i+1, curSum+candidates[i], curList)
                curList.pop()

        
        candidates.sort()
        findTargetSum(0, 0, [])

        return result

        

