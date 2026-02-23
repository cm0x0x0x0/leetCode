class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countTable = [0] * 26

        for c in magazine:
            countTable[ord(c)-ord('a')] += 1
        
        for c in ransomNote:
            if countTable[ord(c)-ord('a')] <= 0:
                return False
            
            countTable[ord(c)-ord('a')] -= 1
        
        return True
