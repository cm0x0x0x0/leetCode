# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        start = head
        while head != None:
            temp.append(head.val)
            head = head.next
        
        idx = len(temp) - 1
        head = start
        while head != None:
            head.val = temp[idx]
            head = head.next
            idx -= 1
        
        return start
