# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recursiveChange(self, start: ListNode, node: ListNode, cnt: int):
        if not cnt:
            start.next = node
            return start, node
        
        head, tail = self.recursiveChange(start, node.next, cnt - 1)
        tail.next = node
        tail = tail.next
        return head, tail
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tempNode = ListNode(0, head)
        iterator = tempNode

        while iterator != None:
            temp = iterator
            flag = True
            for i in range(k):
                if not temp.next:
                    flag = False
                    break
                temp = temp.next
            
            if not flag:
                break

            temp = temp.next
            begin, end = self.recursiveChange(iterator, iterator.next, k - 1)
            end.next = temp
            iterator = end

        return tempNode.next    