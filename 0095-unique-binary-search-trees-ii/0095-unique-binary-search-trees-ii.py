# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def gen_trees(start, end):
            if start > end:
                return [None,]

            ans = []
            for i in range(start, end + 1):
                l = gen_trees(start, i-1)
                r = gen_trees(i+1, end)

                for x in l:
                    for y in r:
                        c = TreeNode(i)
                        c.left = x
                        c.right = y
                        ans.append(c)
            return ans
        return gen_trees(1, n)