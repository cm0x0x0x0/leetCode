class Solution:
    def reverseWords(self, s: str) -> str:
        result = ''
        splitList = s.strip().split(' ')

        result = splitList[-1]
        for i in range(len(splitList)-2, -1, -1):
            if splitList[i] == '':
                continue
            result += ' ' + splitList[i]
        
        return result
        