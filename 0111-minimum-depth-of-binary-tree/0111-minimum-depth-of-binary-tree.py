# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 10 ** 5 + 1
        d = [(root, 1)]
        while d:
            node, height = d.pop()
            if not (node.left or node.right):
                ans = min(ans, height)
            
            if node.left:
                d.append((node.left, height + 1))
            if node.right:
                d.append((node.right, height + 1))
        return ans