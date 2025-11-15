# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        s = set()
        result = ListNode(head.val)
        node = result
        s.add(result.val)
        cur = head.next
        
        while cur != None:
            if cur.val not in s:
                s.add(cur.val)
                node.next = ListNode(cur.val)
                node = node.next

            cur = cur.next
        
        return result


