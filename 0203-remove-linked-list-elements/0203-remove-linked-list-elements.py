# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        before = None

        while cur:
            if cur.val != val:
                before = cur
                cur = cur.next
                continue

            if before == None:
                head = head.next
                cur = head
            else:
                before.next = cur.next
                cur = cur.next                     

        return head

            

        
        return head