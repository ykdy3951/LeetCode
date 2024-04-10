# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = deque()
        node = head
        cnt = 0

        while node:
            if len(d) == n+1:
                d.popleft()
            d.append(node)
            node = node.next
            cnt += 1

        if cnt == n:
            target = d.popleft()
            head = target.next

        if len(d) == n + 1:
            prev = d.popleft()
            target = d.popleft()
            prev.next = target.next

        return head