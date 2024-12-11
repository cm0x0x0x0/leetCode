class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        length = len(s)

        specialCases = {
            "I": ["V", "X"],
            "X": ["L", "C"],
            "C": ["D", "M"]
        }

        transferTable = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        idx = 0

        while idx < length:
            if idx+1 < length:
                if s[idx] in specialCases and s[idx+1] in specialCases[s[idx]]:
                    result += transferTable[s[idx + 1]] - transferTable[s[idx]]
                    idx += 2
                    continue
            
            result += transferTable[s[idx]]
            idx += 1

        return result
