# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional

class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        """
        Wrap around method
        Time: O(m+n); Space: O(1)
        """
        curA = headA
        curB = headB

        # Traverse both lists; when reaching the end of one list, continue at the head of the other list
        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA

        return curA
