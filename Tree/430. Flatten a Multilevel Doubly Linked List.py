"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        curr = head
        dettach = []   

        while curr:
            if curr.child:
                if curr.next:
                    curr.next.prev = None
                    dettach.append(curr.next)

                curr.next = curr.child
                curr.next.prev = curr
                curr.child = None

            if not curr.next and dettach:
                new = dettach.pop()
                curr.next = new
                new.prev = curr
            
            curr = curr.next


        return head
        
