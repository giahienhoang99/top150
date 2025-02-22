def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummyHead = ListNode(0, head)
    prev, cur = dummyHead, head
    while cur and cur.next:
        nxt = cur.next
        nxt2 = nxt.next
        # rewire
        prev.next = nxt
        nxt.next = cur
        cur.next = nxt2
        # shift
        prev = cur
        cur = cur.next
    return dummyHead.next
