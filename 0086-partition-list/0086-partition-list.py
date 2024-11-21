# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        larger = ListNode()
        tail = larger
        traversal = head
        
        # Remove larger start
        while traversal and traversal.val >= x:
            tail.next = traversal
            traversal = traversal.next
            tail = tail.next
            tail.next = None

        head = traversal

        if not head:
            return larger.next
        
        while traversal and traversal.next:
            if traversal.next.val >= x:
                tail.next = traversal.next
                traversal.next = traversal.next.next
                tail = tail.next
                tail.next = None
            else:
                traversal = traversal.next

        traversal.next = larger.next if larger.next else None
        return head