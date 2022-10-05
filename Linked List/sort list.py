# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Will need to review later on, this is still very complicated
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getMid(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
            
        def merge(left, right):
            tail = dummy = ListNode()
            while left and right:
                if left.val < right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next
            if left:
                tail.next = left
            if right:
                tail.next = right

            return dummy.next


        if not head or not head.next:
            return head
        
        #split the list into 2 halfs
        left = head
        right = getMid(head)
        tmp = right.next
        right.next = None
        right = tmp

        left = sortList(left)
        right = sortList(right)
        return merge(left, right)

