# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
import heapq


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        """
        level order traversal to get list of level sums
        is num levels < k return -1
        """
        pq = []
        q = collections.deque([root])
        
        while q:
            level_sum = 0
            for _ in range(len(q)):
                cur = q.popleft()
                level_sum += cur.val
                
                if cur.left: 
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            if len(pq) < k:
                heapq.heappush(pq, level_sum)
                continue

            if len(pq) >= k and level_sum > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, level_sum)
            
        return pq[0] if len(pq) == k else -1

            
    
