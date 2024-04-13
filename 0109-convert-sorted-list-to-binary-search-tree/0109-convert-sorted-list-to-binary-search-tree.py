# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        one_step_node = head
        two_step_node = head
        target = one_step_node
        while two_step_node and two_step_node.next:
            target = one_step_node
            one_step_node = one_step_node.next
            two_step_node = two_step_node.next.next
        root = ListNode(one_step_node.val)
        target.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(one_step_node.next)
        return root