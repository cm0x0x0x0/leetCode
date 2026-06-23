class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left = 0
        right = len(height)-1
        
        while left < right:
            cur = (right-left) * min(height[left], height[right])
            if cur > result:
                result = cur

            if height[left] <= height[right]:
                left +=1
            else:
                right -=1

        return result