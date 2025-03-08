# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def recursiveDepth(node):
            if not node:
                return 0

            left = recursiveDepth(node.left)
            if left == -1:
                return -1
            
            right = recursiveDepth(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return max(left, right) + 1
            
        return recursiveDepth(root) != -1