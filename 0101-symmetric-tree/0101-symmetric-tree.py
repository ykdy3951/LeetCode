# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        d = deque()
        d.append((root.left, root.right))
        while d:
            left, right = d.pop()
            if not left and not right:
                continue
            elif not left or not right:
                return False
            if left.val != right.val:
                return False

            d.append((left.left, right.right))
            d.append((left.right, right.left))
        return True