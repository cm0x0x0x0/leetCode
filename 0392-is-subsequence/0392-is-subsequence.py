class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        curIdx = 0

        if len(s) == 0:
            return True

        for c in t:
            if c == s[curIdx]:
                curIdx += 1
                if curIdx == len(s):
                    break

        return curIdx == len(s)
        