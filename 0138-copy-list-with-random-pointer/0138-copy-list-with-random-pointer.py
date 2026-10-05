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
            nodeTable[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        copyCur = copyHead
        while cur:
            node = nodeTable[cur]
            node.next = nodeTable.get(cur.next)
            node.random = nodeTable.get(cur.random)
            cur = cur.next
        
        return nodeTable[head]
        



