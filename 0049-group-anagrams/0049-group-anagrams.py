class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        tables = []
        rSize = 0


        def newTable(s):
            if s == "":
                return dict({"-1": 1})

            table = dict()
            for c in s:
                if c not in table:
                    table[c] = 1
                    continue
                
                table[c] += 1

            return table

        tables.append(newTable(strs[0]))
        result.append([strs[0]])

        for idx in range(1, len(strs)):
            candTable = newTable(strs[idx])
            find = True
            for j, table in enumerate(tables):
                find = True
                if len(result[j][0]) != len(strs[idx]):
                    find = False
                    continue

                for k, v in table.items():
                    if k not in candTable:
                        find = False
                        break
                    
                    if candTable[k] != v:
                        find = False
                        break

                # find Table
                if find:
                    result[j].append(strs[idx])
                    break
            
            if not find:
                tables.append(candTable)
                result.append([strs[idx]])

        return result
        

