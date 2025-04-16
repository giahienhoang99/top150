class DSU:
    def __init__(self, N):
        self.parent = list(range(N))  # [0,1,2,3,4..N-1]
        self.size = [1] * N

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Supreme leaders
        xr, yr = self.find(x), self.find(y)

        if xr == yr:
            return False

        if self.size[xr] < self.size[yr]:
            xr, yr = yr, xr

        self.size[xr] += self.size[yr]
        self.size[yr] = self.size[xr]
        self.parent[yr] = xr
        return True


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        """
        grid = []
        result = []

        init dsu(m * n)

        convert 2d to 1d: (row, col) -> i
        => row * n + col

        count = 0
        for x, y in positions:
            - change grid[x][y]
            - count += 1
            - check xem neighbors co = 1 k:
                - if ok
                    - if dsu.find(cur) != dsu.find(neighbor):
                        -> count -= 1
                    - union(cur, neighbor)
                - else cont
            - append count to res
        return res
        """
        DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        grid = [[0] * n for i in range(m)]
        dsu = DSU(m * n)
        result = []
        count = 0

        for x, y in positions:

            if grid[x][y] == 1:
                result.append(count)
                continue

            grid[x][y] = 1
            cur = x * n + y
            count += 1

            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if grid[nx][ny] == 1:
                    nb = nx * n + ny
                    if dsu.union(cur, nb):
                        count -= 1
            result.append(count)

        return result
