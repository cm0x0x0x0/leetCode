class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        startPoint = 0
        leftGas = 0
        i = 0

        while i < len(gas):
            leftGas += gas[i]
            leftGas -= cost[i]

            if leftGas < 0:
                startPoint = i+1
                leftGas = 0
                
            i = i+1
        
        return startPoint
            
        

            