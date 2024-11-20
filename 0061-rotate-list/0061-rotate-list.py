# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        n = 0
        nhead = head
        last = None
        while nhead:
            n += 1
            if not nhead.next:
                last = nhead
            nhead = nhead.next
            
        k %= n

        if k == 0:
            return head

        k = n - k        
        nhead = head

        while k - 1:
            nhead = nhead.next
            k -= 1

        node = nhead.next
        nhead.next = None
        last.next = head
        return node


