# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        start = head 
        lista = []
        while (start):
            lista.append(start.val)
            start=start.next
        rez= ListNode()
        current = rez
        lista.reverse()
        for value in lista:
            current.next = ListNode(value)
            current = current.next
        return rez.next