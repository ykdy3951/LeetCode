# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        iterA = headA
        iterB = headB

        while iterA != iterB:
            iterA = iterA.next if iterA else headB
            iterB = iterB.next if iterB else headA

        return iterB