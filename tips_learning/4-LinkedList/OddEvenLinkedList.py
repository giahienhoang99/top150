from typing import Optional


def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # cur_index = 0 => val to track the index of the currently processed node
    # dummy1, dummy2 = pointing to 2 lists: nodes with odd i and those with even i
    # cur_odd, cur_even = None pointers for processing the odd and even lists
    dummy1, dummy2 = ListNode(0, None), ListNode(0, None)
    cur_index, cur_odd, cur_even = 1, dummy1, dummy2
    prev = dummy1

    while head:
        # if even
        if cur_index % 2 == 0:
            # remove it from the original list aka odd list
            prev.next = head.next
            # add to even list
            cur_even.next = head
            # move cur_even forward
            cur_even = cur_even.next
        # if odd
        else:
            cur_odd.next = head
            # move cur_odd forward
            cur_odd = cur_odd.next
            # move prev forward only when head is odd
            prev = head
        # move forward
        head = head.next
        cur_index += 1

    cur_even.next = None
    cur_odd.next = dummy2.next  # connect the 2 lists: last node of odd to first of even

    return dummy1.next
