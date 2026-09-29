import collections
from typing import List

"""Topo sort: BFS"""


def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    indegrees = [0] * numCourses
    graph = collections.defaultdict(list)
    for a, b in prerequisites:
        # a needs b
        # this dict maps nodes to their dependants
        graph[b].append(a)
        # increase indegree of a (the dependant)
        indegrees[a] += 1

    # init queue with nodes having indegree = 0
    q = collections.deque(
        [course for course in range(numCourses) if indegrees[course] == 0]
    )
    count = 0
    while q:
        cur = q.popleft()
        count += 1
        # decrease dependants' indegree by 1
        for dependant in graph[cur]:
            indegrees[dependant] -= 1
            if indegrees[dependant] == 0:
                q.append(dependant)

    return count == numCourses


"""Topo sort: DFS"""
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = collections.defaultdict(list)
    for a, b in prerequisites:
        # a needs b => this dict maps nodes to their dependants
        graph[b].append(a)

    visited = set()  # big set
    ancestors = set()  # set tracking ancestors in cur dfs exploration/path

    # dfs topo
    def dfs(node):
        # node seen in ancestors => found a cycle
        if node in ancestors:
            return False
        # if node visited, no need to check again
        if node in visited:
            return True

        # add to cur path
        ancestors.add(node)
        visited.add(node)
        # go deeper for each new node
        for dependant in graph[node]:
            if dfs(dependant) == False:
                return False
        # remove when finsih exploring
        ancestors.remove(node)
        return True

    for course in list(graph.keys()):
        if dfs(course) == False:
            return False

    return True
