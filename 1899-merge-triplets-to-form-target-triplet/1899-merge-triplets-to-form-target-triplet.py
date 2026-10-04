class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        n = len(triplets)
        cur = [0, 0, 0]

        for tri in triplets:
            skip = False
            for i in range(3):
                if tri[i] > target[i]:
                    skip = True
                    break

            if skip:
                continue

            cur = [
                max(cur[0], tri[0]),
                max(cur[1], tri[1]),
                max(cur[2], tri[2])
            ]
            
        for i in range(3):
            if cur[i] != target[i]:
                return False
        
        return True

            
