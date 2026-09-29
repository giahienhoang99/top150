class DSU:
    def __init__(self, N):
        self.parent = list(range(N))  # initial list of disjoint sets
        self.size = [1] * N  # size list of each set

    def find(self, x):
        """
        Find the root parent of node x. If first time finding x's root parent,
        perform recursion then set self.parent[x] in class DSU to root parent.
        """
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union of x and y by size"""
        # get root parents of both
        xr, yr = self.find(x), self.find(y)

        if xr == yr:
            return False  # skip if already in same set

        if self.size[xr] < self.size[yr]:  # ensure xr is the one with greater size
            xr, yr = yr, xr

        self.parent[yr] = xr
        self.size[xr] += self.size[yr]
        self.size[yr] = self.size[xr]
        return True


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRECTIONS = [(-1, 0), (0, 1), (0, 1), (1, 0)]
        M, N = len(grid), len(grid[0])
        dsu = DSU(M * N)
        count = 0

        for r in range(M):
            for c in range(N):

                if grid[r][c] == "1":
                    u = r * N + c
                    count += 1

                    for dr, dc in DIRECTIONS:
                        nr, nc = r + dr, c + dc

                        if not (0 <= nr < M and 0 <= nc < N):
                            continue
                        if grid[nr][nc] != "1":
                            continue

                        v = nr * N + nc
                        if dsu.union(u, v):
                            count -= 1

        return count
