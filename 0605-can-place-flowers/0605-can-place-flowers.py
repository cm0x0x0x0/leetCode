class Const:
    FREE = 0
    PLANTED = 1

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        plantedCount = 0
        size = len(flowerbed)

        if n == 0:
            return True

        if size == 1:
            return flowerbed[0] == Const.FREE

        # left border
        if flowerbed[0] == Const.FREE:
            if flowerbed[1] == Const.FREE:
                flowerbed[0] = Const.PLANTED
                plantedCount += 1
            

        # middle
        for idx in range(1, size-1):
            if flowerbed[idx] != Const.FREE:
                continue
            
            if flowerbed[idx-1] != Const.FREE:
                continue
            
            if flowerbed[idx+1] != Const.FREE:
                continue
            
            flowerbed[idx] = Const.PLANTED
            plantedCount += 1

        # right border
        if flowerbed[size-1] == Const.FREE:
            if flowerbed[size-2] == Const.FREE:
                flowerbed[size-1] = Const.PLANTED
                plantedCount += 1

        return plantedCount >= n
        
