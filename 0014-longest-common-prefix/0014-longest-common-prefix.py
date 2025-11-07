class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        k = 0
        strsLen = len(strs)
        minLen = min((len(s) for s in strs), default = 0)
        
        for i in range(minLen):
            c = strs[0][i]
            for j in range(1, strsLen):
                if c != strs[j][i]:
                    return strs[0][:k]
            k += 1
        

        return strs[0][k]