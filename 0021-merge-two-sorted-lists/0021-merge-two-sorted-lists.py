# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    maxNum = 101

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        result = head
        
        cur1 = list1
        cur2 = list2
        while True:
            if cur1 == None and cur2 == None:
                break
            
            num1, num2 = self.maxNum, self.maxNum

            if cur1 != None:
                num1 = cur1.val
            
            if cur2 != None:
                num2 = cur2.val
            
            if num1 <= num2:
                result.next = ListNode(num1)
                result = result.next
                if cur1 != None:
                    cur1 = cur1.next
            else:
                result.next = ListNode(num2)
                result = result.next
                if cur2 != None:
                    cur2 = cur2.next
        
        return head.next

            

            
        