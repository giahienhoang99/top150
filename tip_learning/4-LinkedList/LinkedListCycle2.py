def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # If never found a cycle => return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
