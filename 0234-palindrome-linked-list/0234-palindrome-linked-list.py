# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        size = 0
        cur = head
        stack = list()

        while cur != None:
            cur = cur.next
            size += 1
        
        odd = (size | 1) == 1

        cur = head
        midIdx = size // 2
        
        for idx in range(midIdx):
            stack.append(cur.val)
            cur = cur.next
        
        if odd:
            cur = cur.next
        
        while cur != None:
            val = stack.pop()
            if val != cur.val:
                return False

            cur = cur.next

        return True
        
