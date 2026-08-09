class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Găsim mijlocul listei (Slow & Fast Pointers)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Inversăm a doua jumătate a listei
        prev, curr = None, slow.next
        slow.next = None # Tăiem lista în două
        
        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
        
        # După buclă, 'prev' este capul listei inversate
        
        # 3. Împletim (Merge) cele două jumătăți
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2