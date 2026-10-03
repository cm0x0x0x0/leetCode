class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        temp = []
        if len(intervals) == 0:
            return [newInterval]

        # insert newInterval
        inserted = False
        for coord in intervals:
            if coord[0] >= newInterval[0] and not inserted:
                temp.append(newInterval)
                inserted = True
            
            temp.append(coord)
        
        if not inserted:
            temp.append(newInterval)
        
        
        # merge interval
        curInterval = temp[0]
        result.append(curInterval)
        for coord in temp[1:]:
            if curInterval[0] <= coord[0] <= curInterval[1]:
                second = max(curInterval[1], coord[1])
                curInterval[1] = second
            else:
                curInterval = coord
                result.append(curInterval)
        
        return result