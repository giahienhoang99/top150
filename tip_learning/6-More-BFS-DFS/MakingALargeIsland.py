from collections import deque
from typing import List


def largestIsland(self, grid: List[List[int]]) -> int:
    # clone grid
    # find all islands, mark each island with their number
    # mark each island with number of cells they have (can use a list/dict)
    # check all 0's and record biggest size of island achievable
    # return max
    n = len(grid)
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    clone = [[val for val in grid[i]] for i in range(n)]
    island_to_count = {}
    island_num = 2

    def mark_island(row, col) -> int:
        q = deque([(row, col)])
        num_cells = 0
        while q:
            x, y = q.popleft()
            clone[x][y] = island_num
            num_cells += 1
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if clone[nx][ny] == 1:
                    # modify cell in clone grid to match island num
                    clone[nx][ny] = island_num
                    q.append((nx, ny))
        return num_cells

    # bfs to mark islands + track num_cells for each island
    for i in range(n):
        for j in range(n):
            if clone[i][j] == 1:
                num_cells = mark_island(i, j)
                island_to_count[island_num] = num_cells
                island_num += 1
                # return if the whole grid is an island
                if num_cells == n * n:
                    return n * n

    # check all 0-cells to record largest island
    max_size = 0
    for i in range(n):
        for j in range(n):
            if clone[i][j] == 0:
                largest_possible = 1  # starts at 1 cuz need to count the flipped 0
                seen = set()
                for dx, dy in DIRECTIONS:
                    nx, ny = i + dx, j + dy
                    if not (0 <= nx < n and 0 <= ny < n):
                        continue
                    # since modified island cells start from 2
                    if clone[nx][ny] == 0:
                        continue
                    if clone[nx][ny] not in seen:
                        largest_possible += island_to_count[clone[nx][ny]]
                        seen.add(clone[nx][ny])
                max_size = max(max_size, largest_possible)

    return max_size
