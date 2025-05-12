from typing import List


class DSU:
    def __init__(self, N):
        self.parent = list(range(N))
        self.size = [1] * N

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)

        if xr == yr:
            return False
        
        if self.size[xr] < self.size[yr]:
            xr, yr = yr, xr
        
        self.size[xr] += self.size[yr]
        self.size[yr] = self.size[xr]
        self.parent[yr] = self.parent[xr]
        
        return True

class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        """
        init dsu size n + 1
        """
        dsu = DSU(n + 1)
        
        for divisor in range(threshold + 1, n + 1):
            for multiple in range(divisor * 2, n + 1, divisor):
                dsu.union(divisor, multiple)

        return [dsu.find(x) == dsu.find(y) for x, y in queries]