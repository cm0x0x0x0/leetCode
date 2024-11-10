class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        countDict = {}
        occurSet = set()

        for n in arr:
            if n not in countDict:
                countDict[n] = 1
            else:
                countDict[n] += 1

        occurSet.update(countDict.values())

        return len(occurSet) == len(countDict)

        
    