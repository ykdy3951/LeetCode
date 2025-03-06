# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def traversal():
            s = [(root, TreeNode(float('-inf')), TreeNode(float('inf')))]
            while s:
                node, min_node, max_node = s.pop()

                if not node:
                    continue

                if not (min_node.val < node.val < max_node.val):
                    if min_node.val > node.val:
                        min_node.val, node.val = node.val, min_node.val
                    else:
                        max_node.val, node.val = node.val, max_node.val
                    return False
                
                s.append((node.left, min_node, node))
                s.append((node.right, node, max_node))
            return True
        
        while True:
            if traversal():
               break

         
