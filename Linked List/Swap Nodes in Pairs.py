# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        prev, curr = dummy, head
        
        while curr and curr.next:
            #save pointers
            nxtPair = curr.next.next
            second = curr.next

            #reverse this pair
            second.next = curr
            curr.next = nxtPair
            prev.next = second

            #update pointers
            prev = curr
            curr = nxtPair
            
        return dummy.next
                