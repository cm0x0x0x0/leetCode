class Solution:
    def compress(self, chars: List[str]) -> int:
        length = len(chars)
        
        answerIdx = 0
        idx = 0
        while idx < length:
            c = chars[idx]
            count = 0
            while idx < length and chars[idx] == c:
                idx += 1
                count += 1
            
            chars[answerIdx] = c
            answerIdx += 1
            if count > 1:
                for digit in str(count):
                    chars[answerIdx] = digit
                    answerIdx += 1
        
        return answerIdx
