from collections import defaultdict, deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        - each tree node has a coordinate tuple (row, col)
        
        solution in mind
        - bfs to divide all tree nodes into columns, queue item is (node, row, col)
        - use a dict of list to store columns (each mapping: col -> nodes from topdown order)
        - sort dict by key (or col) and turn the dict to a list of lists
        """
        columns = defaultdict(list)
        q = deque([(root, 0, 0)])
        min_col, max_col = 0, 0
        while q:
            for _ in range(len(q)):
                node, row, col = q.popleft()
                # add node to col
                columns[col].append((row, node.val))
                if node.left:
                    min_col = min(min_col, col - 1)
                    q.append((node.left, row + 1, col - 1))
                if node.right:
                    max_col = max(max_col, col + 1)
                    q.append((node.right, row + 1, col + 1))

        result = []
        for i in range(min_col, max_col + 1):
            result.append([t[1] for t in sorted(columns[i])])
        
        return result