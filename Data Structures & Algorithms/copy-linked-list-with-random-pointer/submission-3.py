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
        
        if not head:
            return None
            
        orgToCopy = {}

        curr = head
        while curr :

            copyNode = Node(curr.val)

            orgToCopy[curr] = copyNode

            curr = curr.next

        for node,copyNode in orgToCopy.items():
            copyNode.next = orgToCopy[node.next] if node.next else None
            copyNode.random = orgToCopy[node.random] if node.random else None

        return orgToCopy[head]
            
