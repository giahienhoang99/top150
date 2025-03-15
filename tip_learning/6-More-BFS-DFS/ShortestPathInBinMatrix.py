from collections import deque
from typing import List


def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    DIRECTIONS = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
    # bfs (level order traversal) from topleft cell to botright cell
    n = len(grid)
    q = deque()
    if grid[0][0] == 0:
        q.append((0, 0))
    visited = set([(0, 0)])
    min_steps = 1
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            if (x, y) == (n - 1, n - 1):
                return min_steps
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if (nx, ny) in visited:
                    continue
                if grid[nx][ny] == 0:
                    q.append((nx, ny))
                    visited.add((nx, ny))
        min_steps += 1
    return -1
