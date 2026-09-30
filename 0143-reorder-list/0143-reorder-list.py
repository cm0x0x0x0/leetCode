# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find half
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        
        rear = slow.next
        slow.next = None
        front = head

        # reverse rear part
        before = None
        cur = rear
        while cur:
            after = cur.next
            cur.next = before
            before = cur
            cur = after
        
        rear = before    

        # merge alternately
        head = front

        while front and rear:
            nextFront = front.next
            front.next = rear
            front = nextFront

            nextRear = rear.next
            rear.next = front
            rear = nextRear
            
        return head