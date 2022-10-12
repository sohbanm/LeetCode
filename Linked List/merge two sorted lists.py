# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None and list2==None:
            return None
        
        curr1, curr2 = list1, list2
        ret = new = ListNode()
        while curr1 or curr2:
            if not curr1:
                new.next = ListNode(curr2.val, None)
                curr2 = curr2.next
            elif not curr2:
                new.next = ListNode(curr1.val, None)
                curr1 = curr1.next
            elif curr1.val == curr2.val:
                new.next = ListNode(curr1.val, ListNode(curr2.val,None))
                curr1 = curr1.next
                curr2 = curr2.next
                new = new.next.next
                continue
            else:
                if curr1.val> curr2.val:
                    new.next = ListNode(curr2.val, None)
                    curr2 = curr2.next
                else:
                    new.next = ListNode(curr1.val, None)
                    curr1 = curr1.next
            new = new.next
                
                
                
        return ret.next