class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        tableByPattern = dict()
        tableByS = dict()
        sList = s.split(' ')

        if len(pattern) != len(sList):
            return False

        for idx in range(len(pattern)):
            if pattern[idx] not in tableByPattern:
                tableByPattern[pattern[idx]] = sList[idx]
            
            if sList[idx] not in tableByS:
                tableByS[sList[idx]] = pattern[idx]
            
            if tableByPattern[pattern[idx]] != sList[idx]:
                return False
            
            if tableByS[sList[idx]] != pattern[idx]:
                return False
        
        return True
            

