class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        result = []
        size = len(digits)

        def dfs(curIdx, curLetter):
            if curIdx == size:
                result.append(curLetter)
                return
            
            for c in table[digits[curIdx]]:
                newLetter = curLetter + c
                dfs(curIdx+1, newLetter)
        
        dfs(0, "")
        return result
