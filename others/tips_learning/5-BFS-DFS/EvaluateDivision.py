from collections import defaultdict, deque
from typing import List


def calcEquation(
    self, equations: List[List[str]], values: List[float], queries: List[List[str]]
) -> List[float]:
    """
    2 ways to use adjacency list
    1. dict in dict
    {
        a: {b: 2.0}
        b: {a: 0.5, c: 3.0}
    }

    2. list of tuple in dict
    {
        a: [(b, 2.0)]
        b: {c: 3.0}
    }
    """
    # form adj list => use dict of dict
    adj = defaultdict(dict)
    for i in range(len(equations)):
        numerator = equations[i][0]
        denominator = equations[i][1]
        weight = values[i]
        adj[numerator][denominator] = weight
        adj[denominator][numerator] = 1 / weight
        adj[numerator][numerator] = adj[denominator][denominator] = 1.0

    def bfs(src_var, dest_var) -> float:
        if src_var not in adj or dest_var not in adj:
            return -1.0
        if src_var == dest_var:
            return 1.0

        q = deque([(src_var, 1.0)])
        visited = set()
        visited.add(src_var)

        while q:
            cur_var, cur_val = q.popleft()
            if dest_var in adj[cur_var]:
                return cur_val * adj[cur_var][dest_var]

            for neighbor, weight in adj[cur_var].items():
                if neighbor not in visited:
                    q.append((neighbor, cur_val * weight))
                    visited.add(neighbor)
        return -1.0

    # calculate queries
    results = []
    for query in queries:
        numerator, denominator = query[0], query[1]
        results.append(bfs(numerator, denominator))

    return results
