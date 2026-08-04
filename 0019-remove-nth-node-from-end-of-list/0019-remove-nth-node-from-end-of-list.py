# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = 1
        cur = head
        size = 0

        while cur:
            size += 1
            cur = cur.next
        
        k = size - n
        if k == 0:
            return head.next
            
        cur = head
        for i in range(k-1):
            cur = cur.next

        if cur.next is not None:
            cur.next = cur.next.next

        return head    
            
            
