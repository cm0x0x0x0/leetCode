class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        alpha1, alpha2 = dict(), dict()

        length1 = len(word1)
        length2 = len(word2)
        
        if length1 != length2:
            return False
        
        for c in word1:
            if c not in alpha1:
                alpha1[c] = 1
            else:
                alpha1[c] += 1
        
        for c in word2:
            if c not in alpha2:
                alpha2[c] = 1
            else:
                alpha2[c] += 1
        
        for key in alpha1.keys():
            if key not in alpha2:
                return False
        
        for key in alpha2.keys():
            if key not in alpha1:
                return False
        
        v1 = list(alpha1.values())
        v2 = list(alpha2.values())
        v1.sort()
        v2.sort()
        
        return v1 == v2
