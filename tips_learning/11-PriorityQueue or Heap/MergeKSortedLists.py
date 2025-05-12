# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        k lists
        heap o(N log k)

        - create list of pointers for lists
        - init a min heap with size k (first elements of k lists in lists)
            + each heap element is (node.val, index of list)
        - pop min node

        [[1,4,5],[1,3,4],[2,6]]
        pointers = [i for i in lists]

        h = [1, 1, 2]
        h = [(1, 0, (1, 1), (2, 2)]
        """
        cur = dummy = ListNode()
        
        pq = [(node.val, i) for i, node in enumerate(lists) if node]
        heapq.heapify(pq)
        
        while pq:
            cur_val, cur_i = heapq.heappop(pq)
            cur.next = lists[cur_i]
            cur = cur.next

            # insert new node
            lists[cur_i] = lists[cur_i].next
            if lists[cur_i]:
                heapq.heappush(pq, (lists[cur_i].val, cur_i))
        
        return dummy.next