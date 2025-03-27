from collections import deque
from typing import List


def shortestPathLength(self, graph: List[List[int]]) -> int:
    """
    given adj list
    state: (cur node, path length, visited nodes)
    """
    N = len(graph)  # number of nodes
    DEST = (1 << N) - 1

    q = deque([(i, 0, 1 << i) for i in range(N)])
    visited = set(q)

    while q:
        u, cur_len, visited_nodes = q.popleft()

        # check if visited all nodes
        if visited_nodes == DEST:
            return cur_len

        # check neighbors
        for v in graph[u]:
            new_state = (v, cur_len + 1, visited_nodes | (1 << v))
            if new_state in visited:
                continue
            # append if new state
            q.append(new_state)
            visited.add(new_state)

    return -1
