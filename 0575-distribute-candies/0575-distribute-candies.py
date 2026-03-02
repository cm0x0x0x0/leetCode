class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        typeSet = set()

        maxCandy = len(candyType) // 2

        for n in candyType:
            typeSet.add(n)
        
        return min(len(typeSet), maxCandy)
        


