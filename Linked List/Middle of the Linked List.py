class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head #use to iterate the list
        count=0
        while curr: #while there is a node (an item the pointer points to)
            count+=1
            curr = curr.next
        mid = count//2
        curr = head #pointing curr to head again
        for i in range(mid):
            curr = curr.next #this loop will stop as soon as mid element is reached
        return curr #this is the middle element of the linked list
