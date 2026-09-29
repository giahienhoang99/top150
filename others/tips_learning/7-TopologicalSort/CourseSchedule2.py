import collections
from typing import List

"""Topo sort using BFS"""

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



"""Topo sort using DFS"""

def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    Topo sort using DFS:
    - visited: track visited nodes to avoid cycles
    - ancestors: track the current recursion stack to detect cycles
    - perform DFS on unvisited nodes
    - append node to result list after visiting all its dependents
    - return [] if found cycle
    """
    graph = collections.defaultdict(list)
    for a, b in prerequisites:
        graph[b].append(a)

    visited = set()
    ancestors = set()
    result = collections.deque()

    def dfs(course):
        if course in ancestors:  # cycle found
            return False
        if course in visited:
            return True

        ancestors.add(course)

        for dependant in graph[course]:
            if dfs(dependant) == False:
                return False

        result.appendleft(course)
        visited.add(course)
        ancestors.remove(course)

        return True

    for course in range(numCourses):
        if dfs(course) == False:
            return []

    return list(result)
