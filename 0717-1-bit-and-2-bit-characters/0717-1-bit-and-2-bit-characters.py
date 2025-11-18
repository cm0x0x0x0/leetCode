class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        idx = 0
        _len = len(bits)
        lastIdx = _len - 1

        while idx < lastIdx:
            if bits[idx] == 0:
                idx += 1
                continue
            
            # 1
            idx += 2
        

        return idx == lastIdx
        

