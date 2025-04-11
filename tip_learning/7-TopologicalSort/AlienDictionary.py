from collections import defaultdict, deque
import itertools
from typing import List


def alienOrder(self, words: List[str]) -> str:
    """
    objective: find topo order for chars of words given in alien dict

    idea:
    - create a directed graph of chars so that a char coming before
      another should be pointing to that other char
    - create indegree list
    - apply kahn's algo to get topo order of chars
    - return result string if no cycle

    Key: find first diff between each adj pair
    words = ["wrt","wrf","er","ett","rftt"]
    graph:
        t: f
        w: e
        r: t
        e: r
        f: _
    indegree:
        e: 1
        f: 1
        t: 1
        r: 1
        w: 0
    """
    graph = defaultdict(set)
    indegree = defaultdict(int)

    # build graph + indegree
    for word, nxt in itertools.pairwise(words):
        # abc, ab => invalid
        if len(word) > len(nxt) and word.startswith(nxt):
            return ""

        for c1, c2 in itertools.zip(word, nxt):
            if c1 == c2:
                continue
            if c2 not in graph[c1]:
                graph[c1].add(c2)
                indegree[c2] += 1
                break

    # add those with indegree = 0
    for c in graph:
        if c not in indegree:
            indegree[c] = 0
    """
        print("Graph:")
        for c in graph:
            print(f"  {c}: {list(graph[c])}")
        print("Indegrees:")
        for c in indegree:
            print(f"  {c}: {indegree[c]}")
        """

    num_chars = len(indegree)
    q = deque(c for c in indegree.keys() if indegree[c] == 0)
    print("start q: ", list(q))
    topo_order = []

    while q:
        print("q: ", list(q))
        u = q.popleft()
        topo_order.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    return "".join(topo_order) if len(topo_order) == num_chars else ""
