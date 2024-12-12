class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        def findMaxNumIdx(gifts):
            idx = -1
            max = 0
            for i, n in enumerate(gifts):
                if n >= max:
                    max = n
                    idx = i
            
            return idx
        
        for i in range(k):
            targetIdx = findMaxNumIdx(gifts)
            root = math.floor(gifts[targetIdx] ** 0.5)
            gifts[targetIdx] = root
        
        return sum(gifts)
