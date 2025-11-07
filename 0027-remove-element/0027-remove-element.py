class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        lastDiffIdx = len(nums)-1

        while i <= lastDiffIdx:
            if nums[i] != val:
                k += 1
                i += 1
                continue

            # equal case
            if nums[lastDiffIdx] != val:
                temp = nums[lastDiffIdx]
                nums[lastDiffIdx] = nums[i]
                nums[i] = temp
                k += 1
                i += 1
            
            lastDiffIdx -= 1
        
        return k
            

                

                    

                    
        

