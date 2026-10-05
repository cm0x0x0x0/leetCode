class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # 1. make status table 
        # ex. status = [ ["A", $PAST_TERM, $REMAIN]]
        PAST_TERM = 1
        REMAIN = 2
        status = [] 
        mappingTable = dict()
        totalTask = len(tasks)
        
        for task in tasks:
            if task not in mappingTable:
                mappingTable[task] = len(status)
                status.append([task, float("-inf"), 1])
                continue
            
            idx = mappingTable[task]
            status[idx][REMAIN] += 1
        
        status.sort(key=lambda x: -x[REMAIN])
        
        # 2. simulation
        term = 0
        processedTask = 0
        while processedTask < totalTask:
            selected = None

            for cur in status:
                # skip exhausted
                if cur[REMAIN] == 0:
                    continue
                
                # still cooldown
                if term - cur[PAST_TERM] <= n:
                    continue
                
                if selected == None or cur[REMAIN] > selected[REMAIN]:
                    selected = cur
            
            if selected != None:
                selected[PAST_TERM] = term
                selected[REMAIN] -= 1
                processedTask += 1

            term += 1

        return term
            

