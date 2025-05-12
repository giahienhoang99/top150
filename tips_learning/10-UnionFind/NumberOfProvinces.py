class DSU:
    def __init__(self, N):
        self.parent = list(range(N)) # [0,1,2,3,4..N-1]
        self.size = [1] * N

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Supreme leaders
        xr, yr = self.find(x), self.find(y)

        if xr == yr: return False

        if self.size[xr] < self.size[yr]:
            xr, yr = yr, xr

        self.size[xr] += self.size[yr]
        self.size[yr] = self.size[xr]
        self.parent[yr] = xr
        return True

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # dsu
        n = len(isConnected)
        dsu = DSU(n)
        
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    dsu.union(i, j)
        
        # set comprehension
        return len({dsu.find(i) for i in range(n)})
