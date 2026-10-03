class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        result = []

        # 1. sorting
        intervals = sorted(intervals, key=lambda x: x[0])
        
        # 2. merge range
        curInterval = intervals[0]
        result.append(curInterval)
        for i in range(1, len(intervals)):
            cand = intervals[i]
            if cand[0] <= curInterval[1] and cand[1] >= curInterval[1]:
                curInterval[1] = cand[1]
            elif cand[0] >= curInterval[0] and cand[1] <= curInterval[1]:
                continue
            else:
                curInterval = cand
                result.append(curInterval)

        return result