from typing import List


def sumRemoteness(self, grid: List[List[int]]) -> int:
    # traverse the grid to get sum of all non-blocked cells
    # use dfs/bfs to mark the islands
    # (for each island track sum of cells and #cells)
    # after each island, sumRemoteness += (total sum - island sum) * #cells

    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()

    def dfs(grid, row, col, visited, island_sum_and_count):
        # dfs to mark island
        for dx, dy in DIRECTIONS:
            nx, ny = row + dx, col + dy
            if not (0 <= nx < len(grid) and 0 <= ny < len(grid)):
                continue
            if (nx, ny) in visited:
                continue
            if grid[nx][ny] == -1:
                continue
            island_sum_and_count[0] += grid[nx][ny]
            island_sum_and_count[1] += 1
            visited.add((nx, ny))
            dfs(grid, nx, ny, visited, island_sum_and_count)

    # get total sum - o(n^2)
    total_sum = 0
    for row in grid:
        for cell in row:
            total_sum += cell if cell != -1 else 0

    sum_remote = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if (i, j) not in visited and grid[i][j] != -1:
                # note: have to use a list instead of 2 vars so that
                # the list data is mutable inside dfs()
                island_sum_and_count = [grid[i][j], 1]
                visited.add((i, j))
                dfs(grid, i, j, visited, island_sum_and_count)
                sum_remote += island_sum_and_count[1] * (
                    total_sum - island_sum_and_count[0]
                )

    return sum_remote
