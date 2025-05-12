from collections import deque
from typing import List


def orangesRotting(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    visited = set()
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()

    num_fresh = 0
    # add rotten oranges to q
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                num_fresh += 1
            if grid[i][j] == 2:
                visited.add((i, j))
                q.append((i, j))
    # if no fresh oranges then cant turn fresh into rotten
    if num_fresh == 0:
        return 0
    # bfs
    minutes = -1
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                # add neightbors to q after checking conditions
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if (nx, ny) in visited:
                    continue
                if grid[nx][ny] != 1:
                    continue
                # turn fresh into rotten
                grid[nx][ny] = 2
                # append tuple of coordinates into q and visited
                q.append((nx, ny))
                visited.add((nx, ny))
                # decrement number of fresh oranges
                num_fresh -= 1
        minutes += 1

    # check if there's still fresh orange
    return minutes if num_fresh == 0 else -1
