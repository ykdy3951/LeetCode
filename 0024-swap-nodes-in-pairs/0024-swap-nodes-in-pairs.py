# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev, cur, next = None, head, head.next
        while cur and cur.next:
            node = cur.next
            if prev:
                prev.next = node
            
            cur.next, node.next = node.next, cur
            prev, cur = cur, cur.next

        return next
        