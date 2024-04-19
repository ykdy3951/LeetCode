# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        d=deque()
        d.append((root, False))
        while d:
            node, vst = d.pop()
            if not node:
                continue

            if vst:
                ans.append(node.val)
            else:
                d.append((node, True))
                d.append((node.right, False))
                d.append((node.left, False))

        return ans