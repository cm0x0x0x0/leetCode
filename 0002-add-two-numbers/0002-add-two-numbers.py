# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        head = result
        

        while l1 and l2:
            num = l1.val + l2.val
            head.val += num
            nextNum = head.val // 10
            head.val = head.val % 10
            head.next = ListNode(nextNum)

            l1 = l1.next
            l2 = l2.next
            
            before = head
            head = head.next

        while l1:
            head.val += l1.val
            nextNum = head.val // 10
            head.val = head.val % 10
            head.next = ListNode(nextNum)

            l1 = l1.next

            before = head
            head = head.next

        while l2:
            head.val += l2.val
            nextNum = head.val // 10
            head.val = head.val % 10
            head.next = ListNode(nextNum)

            l2 = l2.next

            before = head
            head = head.next


        if head.val == 0:
            before.next = None

        return result
