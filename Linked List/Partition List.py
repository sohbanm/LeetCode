# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        left = Lptr = ListNode()
        right = Rptr = ListNode()


        while curr:
            nxt = curr.next
            if curr.val < x:
                Lptr.next = ListNode(curr.val, None)
                Lptr = Lptr.next
                curr.next = None
                curr = nxt
                
            else:
                Rptr.next = ListNode(curr.val, None)
                Rptr = Rptr.next
                curr = nxt
        Lptr.next = right.next
        
        return left.next