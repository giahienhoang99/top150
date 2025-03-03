from collections import deque
from typing import List


def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    # notice: left + top edge can flow to pacific
    #        right + bot edge can flow to atlantic
    # what if go from the 2 oceans?
    #

    m, n = len(heights), len(heights[0])

    def get_reachable_set(q) -> set:
        reachables = set(q)
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            x, y = q.popleft()
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if (nx, ny) in reachables:
                    continue
                if heights[nx][ny] >= heights[x][y]:
                    q.append((nx, ny))
                    reachables.add((nx, ny))
        return reachables

    res = []
    pacific_q = deque([(i, 0) for i in range(m)] + [(0, j) for j in range(n)])
    atlantic_q = deque([(i, n - 1) for i in range(m)] + [(m - 1, j) for j in range(n)])

    pacific_set = get_reachable_set(pacific_q)
    atlantic_set = get_reachable_set(atlantic_q)

    return list(pacific_set & atlantic_set)
