from collections import deque
from typing import List

def shortestBridge(self, grid: List[List[int]]) -> int:
    # find first island by
    #   - traversing thru the grid until found a 1
    #   - bfs on that 1 to get the whole island (if exist other 1's) -> store in a set
    # for each of these 1's, do bfs to count steps to reach island 2
    #   - use a min_steps var to continuosly update the min steps

    # square grid
    n = len(grid)
    q = deque()
    island1_set = set()
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # find first 1 and break
    found = False
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                q.append((i, j))
                island1_set.add((i, j))
                found = True
                break
        if found:
            break

    # mark 1st island
    while q:
        x, y = q.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if (nx, ny) in island1_set:
                continue
            if grid[nx][ny] == 1:
                q.append((nx, ny))
                island1_set.add((nx, ny))

    # bfs from each node of island 1 to find island 2
    q = deque([(i, j) for i, j in island1_set])
    visited = set(island1_set)
    dist = 0

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if (nx, ny) in visited:
                    continue
                if grid[nx][ny] == 1:  # found island 2
                    return dist
                q.append((nx, ny))
                visited.add((nx, ny))
        dist += 1

    return -1  # shouldnt reach here
