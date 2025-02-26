from collections import deque
from typing import List

# dfs
def numIslands(self, grid: List[List[str]]) -> int:
    m, n = len(grid), len(grid[0])
    count_islands = 0
    visited = set()  # set of tuple
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(x, y) -> None:
        visited.add((x, y))
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < m and 0 <= ny < n):
                continue
            if grid[nx][ny] == "0":
                continue
            if (nx, ny) in visited:
                continue
            dfs(nx, ny)

    for i in range(m):
        for j in range(n):
            cur = (i, j)
            if cur not in visited and grid[i][j] == "1":
                dfs(i, j)
                count_islands += 1

    return count_islands

# bfs
def numIslandsBFS(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count_islands = 0
        visited = set() # set of tuple
        DIRECTIONS = [(-1,0), (1,0), (0,-1), (0,1)]
        
        def bfs(grid, visited, x, y) -> None:
            q = deque()
            q.append((x,y))
            while q:
                x, y = q.popleft()
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in visited:
                        continue
                    if not (0 <= nx < m) or not (0 <= ny < n):
                        continue
                    if grid[nx][ny] == "0":
                        continue
                    q.append((nx, ny))
                    visited.add((nx, ny))

        for i in range(m):
            for j in range(n):
                cur = (i, j)
                if cur not in visited and grid[i][j] == "1":
                    bfs(grid, visited, i, j)
                    count_islands += 1   
        
        return count_islands