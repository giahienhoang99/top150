def mergeTwoLists(
    self, list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    # use dummy head aka sentinel node to start the result list
    dummy = ListNode(0, None)
    cur = dummy
    # connect cur node to the smaller of the current heads of 2 lists and update accordingly
    while list1 and list2:
        if list1.val <= list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next
    # after 1 list pointer becomes null
    # => we just connect the cur node to the head of the remaining list
    cur.next = list1 if list1 else list2

    return dummy.next
