class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        table = dict()
        partitions = []
        curIdx = 0

        for char in s:
            if char in table:
                tableIdx = table[char]
                for i in range(tableIdx+1, curIdx):
                    partitions[tableIdx] += partitions[i]
                    for c in partitions[i]:
                        table[c] = tableIdx

                    partitions[i] = ""
                
                partitions[tableIdx] += char
                curIdx = tableIdx+1
                continue
            
            if len(partitions) <= curIdx:
                partitions.append(char)
            else:
                partitions[curIdx] += char

            table[char] = curIdx
            curIdx += 1
        

        result = []
        for part in partitions:
            if part == "":
                continue
            
            result.append(len(part))
        
        return result