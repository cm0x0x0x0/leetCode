class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = [0] * (len(gain)+1)
        curAltitude = 0
        
        for idx in range(len(gain)):
            curAltitude += gain[idx]
            altitude[idx+1] = curAltitude
        
        return max(altitude)
        