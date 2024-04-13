# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def make_bst(nums: List[int]) -> Optional[TreeNode]:
            if len(nums) == 1:
                return TreeNode(nums[0])
            if len(nums) == 2:
                node = TreeNode(nums[1])
                node.left = TreeNode(nums[0])
                return node
            root_idx = len(nums) // 2
            root = TreeNode(nums[root_idx])
            root.left = make_bst(nums[:root_idx])
            root.right = make_bst(nums[root_idx+1:])
            return root
        return make_bst(nums)