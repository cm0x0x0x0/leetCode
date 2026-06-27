class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        last = {}
        start = 0
        end = 0

        for idx, c in enumerate(s):
            last[c] = idx
        

        for idx, c in enumerate(s):
            end = max(end, last[c])

            if idx == end:
                result.append(end-start+1)
                start = end+1
        
        return result

