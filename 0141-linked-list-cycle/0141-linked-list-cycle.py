# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        table = set()

        while head != None:
            if id(head) in table:
                return True
            
            table.add(id(head))
            head = head.next

        return False