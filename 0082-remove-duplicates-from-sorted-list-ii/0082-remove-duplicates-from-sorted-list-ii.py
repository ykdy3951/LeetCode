# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode()
        tail = dummy
        
        while head and head.next:
            if head.next.val != head.val:
                tail.next = ListNode(head.val)
                tail = tail.next
            else:
                while head.next and head.next.val == head.val:
                    head = head.next

            head = head.next

        if head:
            tail.next = ListNode(head.val)

        return dummy.next