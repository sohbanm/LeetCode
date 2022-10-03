#___________Using Stacks Method__________
# class Solution:
#     def reverseString(self, s: list[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         stack = []
#         for char in s:
#             stack.append(char)

#         i = 0
#         while stack:
#             s[i] = stack.pop()
#             i+=1
#         print(s)

#_______Using Recursion Method_____
# class Solution:
#     def reverseString(self, s: list[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         def reverse(l,r):
#             if l < r:
#                 s[l], s[r] = s[r], s[l]
#                 reverse(l+1, r-1)

#         reverse(0,len(s)-1)
#         print(s)

#____________Two Pointers method (Most Efficient)________
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l,r = 0, len(s)-1

        while l<=r:
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
        print(s)

sol = Solution()
sol.reverseString(s = ["h","e","l","l","o"])