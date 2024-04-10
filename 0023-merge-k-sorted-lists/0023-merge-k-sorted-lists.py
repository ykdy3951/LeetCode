# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        tail = head
        dic = defaultdict(int)

        for temp in lists:
            while temp:
                dic[temp.val] += 1
                temp = temp.next

        for key in sorted(list(dic.keys())):
            for _ in range(dic[key]):
                tail.next = ListNode(key)
                tail = tail.next

        return head.next