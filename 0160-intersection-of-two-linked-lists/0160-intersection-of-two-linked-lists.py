# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        aLen = 0
        bLen = 0
        pA = headA
        pB = headB
        while pA:
            aLen += 1
            pA = pA.next
        
        while pB:
            bLen += 1
            pB = pB.next

        maxIter = aLen + bLen
        pA = headA
        pB = headB
        for i in range(maxIter):
            if pA == pB:
                return pA
            
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return None