# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 1
        node = root
        q = deque()
        if not node:
            return 0
        q.append([node, 1])
        while q:
            now, depth = q.pop()
            ans = max(ans, depth)

            if now.left:
                q.append([now.left, depth + 1])
            if now.right:
                q.append([now.right, depth + 1])

        return ans          