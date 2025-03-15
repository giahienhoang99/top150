import collections
from typing import List


def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    Kahn's algo:
    0. Calculate the in-degree of all vertices
    1. Setup a queue with all vertices that has ZERO indegree; setup a result list
    2. While queue is not empty:
        a. Pop the vertice out of our queue, and add to the result list (call it u)
        b. Remove the vertice entirely from the graph (just imagination)
        c. For each neighbor v of the removed vertice, decrement the indegree of v by 1.
        d. Add v to queue if indegree v is 0
    We have a toposort <=> len(result) == N
    """
    graph = collections.defaultdict(list)
    indegrees = [0] * numCourses
    for a, b in prerequisites:
        indegrees[a] += 1
        graph[b].append(a)

    q = collections.deque(u for u in range(numCourses) if indegrees[u] == 0)
    result = []

    while q:
        u = q.popleft()
        result.append(u)
        for v in graph[u]:
            indegrees[v] -= 1
            if indegrees[v] == 0:
                q.append(v)

    return result if len(result) == numCourses else []
