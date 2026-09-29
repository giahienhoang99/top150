from collections import deque
from typing import List


def swimInWater(self, grid: List[List[int]]) -> int:
    # square grid
    n = len(grid)
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def can_reach_with_t(t) -> bool:
        # bro cant even enter the starting point
        if grid[0][0] > t:
            return False

        q = deque([(0, 0)])
        visited = set([(0, 0)])

        while q:
            x, y = q.popleft()
            if (x, y) == (n - 1, n - 1):
                return True
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if (nx, ny) in visited:
                    continue
                if grid[nx][ny] > t:
                    continue
                q.append((nx, ny))
                visited.add((nx, ny))
        return False

    # binary search + bfs
    t = 0
    l, r = 0, n * n
    while l <= r:
        mid = (l + r) // 2
        if can_reach_with_t(mid):
            t = mid
            r = mid - 1
        else:
            l = mid + 1
    return t
