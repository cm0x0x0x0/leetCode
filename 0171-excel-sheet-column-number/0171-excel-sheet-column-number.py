class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        table = dict()

        for n in range(ord('A'), ord('Z')+1):
            table[chr(n)] = n - 65
        
        for idx,c in enumerate(columnTitle[::-1]):
            result += (table[c]+1) * pow(26, idx)

        return result
            