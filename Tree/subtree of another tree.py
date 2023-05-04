# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if self.isSameTree(root, subRoot):
            return True
        else:
            if not root:
                return False
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if (not p or not q) or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(q.right, p.right)