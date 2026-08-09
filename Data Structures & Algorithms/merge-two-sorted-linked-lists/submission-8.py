# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start1 = list1
        start2 = list2
        rez = ListNode(0)
        current = rez

        while (start1 and start2):
            if start1.val < start2.val:
                current.next = start1
                start1 = start1.next
            else:
                current.next = start2
                start2 = start2.next
            current = current.next
        if start1:
            current.next = start1 
        elif start2:
            current.next = start2
        return rez.next
