# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        table = set()
        listA = headA
        listB = headB

        while listA:
            table.add((id(listA), listA))
            listA = listA.next
        
        while listB:
            if (id(listB), listB) in table:
                return listB
            
            table.add((id(listB), listB))
            listB = listB.next

        return None