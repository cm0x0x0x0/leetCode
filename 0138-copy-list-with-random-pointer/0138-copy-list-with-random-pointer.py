"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None

        nodeTable = {} # key: original node pointer, val: node
        copyHead = Node(x=-1) # dummy

        cur = head
        while cur:
            node = Node(cur.val)
            nodeTable[cur] = node
            cur = cur.next

        cur = head
        copyCur = copyHead
        idx = 0
        while cur:
            node = nodeTable[cur]
            copyCur.next = node
            if cur.next != None:
                node.next = nodeTable[cur.next]
            
            cur = cur.next
            copyCur = copyCur.next
        

        cur = head
        copyCur = copyHead.next 
        while cur:
            if cur.random != None:
                copyCur.random = nodeTable[cur.random]
            
            cur = cur.next
            copyCur = copyCur.next
        
        return copyHead.next
        



