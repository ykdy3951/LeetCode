# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        d=deque()
        if root:
            d.append((root, 0))
        while d:
            node, depth = d.popleft()

            if len(ans) <= depth:
                ans.append([])

            ans[depth].append(node.val)

            if node.left:
                d.append((node.left, depth + 1))
            if node.right:
                d.append((node.right, depth + 1))
            
        return ans