from collections import deque
from typing import List


def levelOrder(self, root: "Node") -> List[List[int]]:
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            cur = q.popleft()
            level.append(cur.val)
            for child in cur.children:
                q.append(child)
        result.append(level)
    return result
