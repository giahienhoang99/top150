from collections import deque
from typing import List


# bfs
def findCircleNum(self, isConnected: List[List[int]]) -> int:
    # form adj list
    # traverse adj list => mark visited using bfs
    n = len(isConnected)
    adj = [[] for _ in range(n)]
    for u in range(n):
        for v in range(u + 1, n):
            if isConnected[u][v]:
                adj[u].append(v)
                adj[v].append(u)
    print(adj)
    q = deque()
    visited = set()

    def mark_all_connected(city):
        q.append(city)
        visited.add(city)
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in visited:
                    q.append(v)
                    visited.add(v)

    num_provinces = 0
    for u in range(n):
        if u not in visited:
            mark_all_connected(u)
            num_provinces += 1

    return num_provinces


# dfs
def findCircleNum(self, isConnected: List[List[int]]) -> int:
    # given the adjacency matrix isConnected
    # use dfs to mark all connected cities of a province and increment num_provinces by 1
    n = len(isConnected)  # given square adj matrix
    num_provinces = 0
    visited = set()

    def mark_all_connected(row) -> None:
        if row not in visited:
            visited.add(row)
            for col in range(n):
                if isConnected[row][col]:
                    mark_all_connected(col)

    for i in range(n):
        if i not in visited:
            mark_all_connected(i)
            num_provinces += 1

    return num_provinces
