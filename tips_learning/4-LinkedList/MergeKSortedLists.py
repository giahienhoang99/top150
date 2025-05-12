class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # brute force: store all nodes in a list -> sort list by node.val -> create sorted linkedlist
        # => O(n*k)
        # in place?
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        # merge every pair of linkedlists => o(logk) * o(n)
        l = len(lists)  # gradually be divided by 2, could be odd or even

        while l > 1:
            i = 0
            next_l = (l + 1) // 2
            for i in range(0, l - 1, 2):
                lists[i // 2] = self.merge(lists[i], lists[i + 1])
            if l % 2 == 1:
                lists[next_l - 1] = lists[-1]
            # trim lists to merged part only
            l = next_l
            lists = lists[:l]
        return lists[0]

    def merge(self, list1, list2):
        dummy = ListNode(0, None)
        cur = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                # update list1
                list1 = list1.next
            else:
                cur.next = list2
                # update list2
                list2 = list2.next
            cur = cur.next
        # add remaining nodes of list1 or list2
        cur.next = list1 if list1 else list2
        return dummy.next