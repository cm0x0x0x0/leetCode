class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result = []
        table = dict()
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"

        for c in row1:
            table[c] = 1
            table[c.upper()] = 1
        
        for c in row2:
            table[c] = 2
            table[c.upper()] = 2
        
        for c in row3:
            table[c] = 3
            table[c.upper()] = 3
        
        for word in words:
            success = True
            targetRow = table[word[0]]
            for c in word:
                if table[c] != targetRow:
                    success = False
                    break

            if success:
                result.append(word)
        
        return result