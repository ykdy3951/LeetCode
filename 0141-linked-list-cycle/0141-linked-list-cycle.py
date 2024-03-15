# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        chk_list = set()
        node=head

        while node:
            if node in chk_list:
                return True
            chk_list.add(node)
            node = node.next
        
        return False
