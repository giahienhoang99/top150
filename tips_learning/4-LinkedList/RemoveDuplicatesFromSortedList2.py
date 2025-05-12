def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(-101, head)
    prev, cur = dummy, head
    while cur:
        if cur.next and cur.val == cur.next.val:
            # move cur forward when cur val == next val
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            # when exit while loop, cur is stil a dup and cur.next is not
            prev.next = cur.next  # skip all duplicates
        else:
            prev = prev.next
        cur = cur.next
    return dummy.next
