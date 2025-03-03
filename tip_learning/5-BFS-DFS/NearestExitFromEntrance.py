from collections import deque
from typing import List


def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
    # how to check that we have reached the exit?
    # point (x, y) is exit if maze[x][y] == '.' and point (x, y) is on the maze's edge
    m, n = len(maze), len(maze[0])
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    min_steps = 0

    row, col = entrance  # remember entrance coords
    q = deque([(row, col)])
    visited = set([(row, col)])

    while q:
        for i in range(len(q)):
            x, y = q.popleft()
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if (nx, ny) in visited:
                    continue
                if maze[nx][ny] != ".":
                    continue
                # check if empty cell is on the edge of the maze and not entrance
                if nx == 0 or ny == 0 or nx == m - 1 or ny == n - 1:
                    return min_steps + 1
                q.append((nx, ny))
                visited.add((nx, ny))
        min_steps += 1

    return -1
