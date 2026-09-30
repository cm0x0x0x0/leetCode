class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        result = []
        table = dict()
        sortedList = []

        for n in nums:
            if n not in table:
                table[n] = 1
            else:
                table[n] += 1
        
        for (n, cnt) in table.items():
            sortedList.append((n, cnt))
        
        sortedList.sort(key=lambda x: x[1], reverse=True)


        for i in range(k):
            result.append(sortedList[i][0])

        return result
            
        