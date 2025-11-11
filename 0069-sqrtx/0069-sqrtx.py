class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        low = 0
        high = x
        mid = int((low+high)/2)

        while low+1<high:
            powVal = mid*mid
            if powVal == x:
                return mid
            
            k = mid+1
            if powVal < x and k*k > x:
                return mid
            
            if powVal < x:
                low = mid
            else:
                high = mid
            
            mid = int((low+high)/2)
            

        return 0