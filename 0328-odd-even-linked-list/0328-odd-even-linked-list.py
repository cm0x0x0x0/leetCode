# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        headNext = head.next
        if headNext == None:
            return head
            
        oddLastNode = ListNode(head.val, None)
        evenLastNode = ListNode(headNext.val, None)
        oddFirstNode = oddLastNode
        evenFirstNode = evenLastNode

        head = head.next.next
        cnt = 3
        while head != None:
            if cnt % 2 == 0:
                evenLastNode.next = ListNode(head.val, None)
                evenLastNode = evenLastNode.next
            else:
                oddLastNode.next = ListNode(head.val, None)
                oddLastNode = oddLastNode.next
            
            head = head.next
            cnt += 1

        oddLastNode.next = evenFirstNode

        return oddFirstNode
        