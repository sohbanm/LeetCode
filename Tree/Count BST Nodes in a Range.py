# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, lo, hi):
        if not root: 
            return 0
        if root.val < lo: return self.solve(root.right, lo, hi)
        if root.val > hi: return self.solve(root.left, lo, hi)
        # if root in the range:
        res = 1 + self.solve(root.right, lo, hi) + self.solve(root.left, lo, hi)
        return res
