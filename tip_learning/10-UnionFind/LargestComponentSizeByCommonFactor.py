from typing import List


class DSU:
    def __init__(self, N):
        self.parent = list(range(N))
        self.size = [1] * N

    def find(self, x) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y) -> bool:
        xroot, yroot = self.find(x), self.find(y)

        if xroot == yroot:
            return False

        if self.size[xroot] < self.size[yroot]:
            xroot, yroot = yroot, xroot
        
        self.parent[yroot] = xroot
        self.size[xroot] += self.size[yroot]
        self.size[yroot] = self.size[xroot]

        return True

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        """
        idea: union find + sieve
        """
        dsu = DSU(len(nums))
        biggest = max(nums)
        num_to_index = {num: i for i, num in enumerate(nums)}

        for p in range(2, biggest + 1):
            first = -1
            # check all multiples of p and if each is in nums
            for multiple in range(p, biggest + 1, p):
                if multiple in num_to_index:
                    if first == -1:
                        first = num_to_index[multiple]
                    else:
                        dsu.union(first, num_to_index[multiple])

        return max(dsu.size)