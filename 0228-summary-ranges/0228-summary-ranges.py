class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
            
        result = []
        head = nums[0]
        before = head

        for i in range(1,len(nums)):
            if nums[i] != before + 1:
                if head == before:
                    result.append(str(head))
                else:
                    result.append(str(head)+"->"+str(before))

                head = nums[i]
                before = head
                continue
            
            before = nums[i]
        
        if head == before:
            result.append(str(head))
        else:
            result.append(str(head)+"->"+str(nums[-1]))

        
        return result