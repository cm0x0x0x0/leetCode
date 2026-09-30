class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        result = []
        table = dict()
        size = len(nums)

        for n in nums:
            if n not in table:
                table[n] = 1
            else:
                table[n] += 1
        
        bucket = [[] for _ in range(size + 1)]

        for n, cnt in table.items():
            bucket[cnt].append(n)
        
        for cnt in range(size, 0, -1):
            for n in bucket[cnt]:
                result.append(n)
            
                if len(result) == k:
                    return result
        
        return []
            
        