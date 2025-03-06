# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        s = deque()
        s.append((root, float('-inf'), float('inf')))
        while s:
            node, min_val, max_val = s.pop()

            if not node:
                continue

            if not (min_val < node.val < max_val):
                return False

            s.append((node.left, min_val, node.val))
            s.append((node.right, node.val, max_val))

        return True