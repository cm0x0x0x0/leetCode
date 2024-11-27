class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        totalRoomNum = len(rooms)
        visited = [False] * totalRoomNum
        visitedCount = 0
        stack = []

        for key in rooms[0]:
            stack.append(key)
        visited[0] = True
        visitedCount += 1
        
        while len(stack) > 0 and visitedCount < totalRoomNum:
            key = stack.pop()
            if visited[key]:
                continue
            
            visited[key] = True
            visitedCount += 1
            
            for candidateKey in rooms[key]:
                stack.append(candidateKey)
            
        return visitedCount == totalRoomNum


