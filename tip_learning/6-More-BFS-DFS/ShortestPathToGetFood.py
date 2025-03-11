from collections import deque
from typing import List


def getFood(self, grid: List[List[str]]) -> int:
    def bfs(row, col, visited) -> int:
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        min_steps = 0
        q = deque([(row, col)])
        visited = set([(row, col)])
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
                        continue
                    if (nx, ny) in visited:
                        continue
                    if grid[nx][ny] == "X":
                        continue
                    if grid[nx][ny] == "#":
                        return min_steps + 1
                    q.append((nx, ny))
                    visited.add((nx, ny))
                # increment for each level traversed
            min_steps += 1
        return -1

    visited = set()
    # find the starting point and start bfs from there
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "*":
                steps = bfs(i, j, visited)

    return steps
