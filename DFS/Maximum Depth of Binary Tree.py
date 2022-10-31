# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Recursive DFS 
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Iterative DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:        
        stack = [[root, 1]]
        res = 0

        while stack:
            root, depth = stack.pop()

            if root:
                res = max(res, depth)
                stack.append([root.left, depth+1])
                stack.append([root.right, depth+1])

        return res


# Iterative BFS   (This traverses the tree level by level)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                root = q.popleft()
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            level += 1
        return level