# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         outputNode = ListNode()

#         #Creates String for the First List
#         first = str(l1.val)
#         while l1.next:
            
#             l1 = l1.next
#             first = str(l1.val) + first

#         #Creates String for the Second List
#         second = str(l2.val)
#         while l2.next:
#             l2 = l2.next
#             second = str(l2.val) + second

#         sum = int(first) + int(second)
        
#         if(len(str(sum)))!=1:
#             curr = outputNode
#             for i in range(len(str(sum))-1,0,-1):
#                 curr.val = sum%10
#                 sum = sum//10
#                 curr.next = ListNode()
#                 curr = curr.next
#             curr.val = sum
#         else:
#             outputNode.val = sum

#         return outputNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = cur = ListNode(0)
        val = 0
        while l1 or l2 or val:
            if l1: 
                val += l1.val
                l1 = l1.next
            if l2: 
                val += l2.val
                l2 = l2.next
            cur.next = cur = ListNode(val%10)
            val //= 10
        return ret.next
    