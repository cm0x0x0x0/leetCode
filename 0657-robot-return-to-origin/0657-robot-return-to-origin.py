class Solution:
    def judgeCircle(self, moves: str) -> bool:
        leftCount = 0
        rightCount = 0
        upCount = 0
        downCount = 0

        for move in moves:
            if move == 'L':
                leftCount += 1
            elif move =='R':
                rightCount += 1
            elif move == 'U':
                upCount += 1
            else:
                downCount += 1
        
        return leftCount == rightCount and upCount == downCount