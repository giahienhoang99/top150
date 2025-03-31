# Definition for a Node
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
from collections import defaultdict, deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        idea: o(n) time and space
        - traverse the graph, use a dict to map node's val -> its neighbors
        - make a new graph with the dict
        """
        if not node:
            return None

        # traverse and store mappings val -> nb vals
        graph = defaultdict(list)
        q = deque([node])
        visited = set([node])

        while q:
            u = q.popleft()
            graph[u.val] = []
            for v in u.neighbors:
                graph[u.val].append(v.val)
                if v not in visited:
                    q.append(v)
                    visited.add(v)

        # rebuild new graph using dict
        node_map = {val: Node(val) for val in graph}

        for val, nbs in graph.items():
            node_map[val].neighbors = [node_map[nb] for nb in nbs]
        
        return node_map[node.val]