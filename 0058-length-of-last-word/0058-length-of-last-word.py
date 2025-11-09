class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        arr = s.split(' ')
        
        for letter in reversed(arr):
            if letter != '':
                return len(letter)
        
        return 1
        
    