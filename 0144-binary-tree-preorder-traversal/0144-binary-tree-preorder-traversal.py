# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans=[]
        d=deque()
        d.append(root)
        while d:
            node=d.pop()
            ans.append(node.val)
            if node.right:
                d.append(node.right)
            if node.left:
                d.append(node.left)
        return ans