class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        level = 0
        q = [root]
        while q:
            for i in range(len(q)):
                root = q.pop(0)
                if not root.left and not root.right:
                    return level+1
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            level += 1