# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0

        # find length
        start = head
        while start != None:
            length += 1
            start = start.next
        
        
        if length == 1:
            return None

        midIdx = length // 2
        # remove mid node
        idx = 0
        start = head
        before = None
        while idx < midIdx:
            before = start
            start = start.next
            idx += 1
        
        before.next = start.next

        return head

        