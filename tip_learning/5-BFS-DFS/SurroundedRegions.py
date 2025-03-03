from collections import deque
from typing import List


def solve(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    m, n = len(board), len(board[0])
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()

    def mark_region(row, col) -> None:
        q = deque([(row, col)])
        while q:
            x, y = q.popleft()
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                # check boundary and if visited
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if (nx, ny) in visited:
                    continue
                # if it's 0, continue bfs on the pair of coords
                if board[nx][ny] == "O":
                    q.append((nx, ny))
                    visited.add((nx, ny))

    # traverse outermost layer to find O's on edge + bfs to mark regions connected to each O as visited
    for i in range(m):
        if board[i][0] == "O" and (i, 0) not in visited:
            visited.add((i, 0))
            mark_region(i, 0)
        if board[i][-1] == "O" and (i, n - 1) not in visited:
            visited.add((i, n - 1))
            mark_region(i, n - 1)
    for j in range(n):
        if board[0][j] == "O" and (0, j) not in visited:
            visited.add((0, j))
            mark_region(0, j)
        if board[-1][j] == "O" and (m - 1, j) not in visited:
            visited.add((m - 1, j))
            mark_region(m - 1, j)

    # if not surrounded region, mark O as X
    for i in range(m):
        for j in range(n):
            if board[i][j] == "O" and (i, j) not in visited:
                board[i][j] = "X"
