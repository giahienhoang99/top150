from collections import deque
from typing import List

# dfs
def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    result = 0
    visited = set()
    DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(x, y, count) -> int:
        count += 1
        visited.add((x, y))
        for dx, dy in DIR:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < m and 0 <= ny < n):
                continue
            if (nx, ny) in visited:
                continue
            if grid[nx][ny] == 0:
                continue
            count = dfs(nx, ny, count)
        return count

    for i in range(m):
        for j in range(n):
            if (i, j) not in visited and grid[i][j] == 1:
                count = 0
                count = dfs(i, j, count)
                result = max(result, count)

    return result

# bfs
def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    result = 0
    visited = set()
    DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(x, y) -> int:
        count = 0
        q = deque([(x, y)])
        visited.add((x, y))
        while q:
            x, y = q.popleft()
            count += 1
            for dx, dy in DIR:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if (nx, ny) in visited:
                    continue
                if grid[nx][ny] == 0:
                    continue
                q.append((nx, ny))
                visited.add((nx, ny))
        return count

    for i in range(m):
        for j in range(n):
            if (i, j) not in visited and grid[i][j] == 1:
                count = bfs(i, j)
                result = max(result, count)

    return result
