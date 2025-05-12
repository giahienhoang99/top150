class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # brute force: can traverse once thru the list and input values in a hashmap
        # then sort the hashmap -> create new linked list from it
        # however, question demands an O(nlogn) time comp and O(1) space comp
        # idea: mergesort but on linkedlist
        # - dividing the list in halves
        # - merging sublists and still remain ascending order

        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # after the loop ends, slow will be at the middle of the list
        right = slow.next
        slow.next = None

        l_half = self.sortList(head)
        r_half = self.sortList(right)

        # merge
        return self.merge(l_half, r_half)

    # merge 2 sorted lists
    def merge(self, l: Optional[ListNode], r: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        cur = dummy
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        # might still be leftover nodes in one list
        if l:
            cur.next = l
        if r:
            cur.next = r
        return dummy.next
