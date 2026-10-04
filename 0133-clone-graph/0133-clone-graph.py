"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        
        maked = dict()
        def makeNode(curNode):
            if curNode.val in maked:
                return maked[curNode.val]

            new = Node(val=curNode.val)
            maked[new.val] = new
            for neighbor in curNode.neighbors:
                new.neighbors.append(makeNode(neighbor))
            
            return new
        
        myNode = makeNode(node)
        
        return myNode
