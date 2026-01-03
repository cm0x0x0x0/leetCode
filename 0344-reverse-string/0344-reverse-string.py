class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lastIdx = len(s)-1
        for i in range(lastIdx//2):
            temp = s[i]
            s[i] = s[lastIdx-i]
            s[lastIdx-i] = temp
        