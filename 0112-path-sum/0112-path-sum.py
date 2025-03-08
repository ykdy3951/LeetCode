# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        d = deque()
        d.append((root, root.val))

        while d:
            node, valSum = d.popleft()

            if not (node.left or node.right):
                if valSum == targetSum:
                    return True

            if node.left:
                d.append((node.left, valSum + node.left.val))
            if node.right:
                d.append((node.right, valSum + node.right.val))
        return False