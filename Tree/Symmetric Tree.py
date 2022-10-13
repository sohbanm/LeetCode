# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def isMirror(lRoot, rRoot):
            if lRoot and rRoot:
                return (lRoot.val == rRoot.val) and (isMirror(lRoot.left, rRoot.right)) and (isMirror(lRoot.right, rRoot.left))
            return lRoot == rRoot

        return isMirror(root.left,root.right)