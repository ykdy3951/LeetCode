# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev_mid = head
        mid = None
        if left == 1:
            mid = head
        else:
            for _ in range(left - 2):
                prev_mid = prev_mid.next
            mid = prev_mid.next

        dummy = mid
        mtail = mid.next
        mhead = dummy

        for _ in range(right - left):
            temp = mtail
            mtail = mtail.next
            temp.next = mhead
            mhead = temp
        
        if left == 1:
            dummy.next = mtail
            return mhead
        else:
            prev_mid.next = mhead
            dummy.next = mtail
            return head

