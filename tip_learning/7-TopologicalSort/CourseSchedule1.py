import collections
from typing import List


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
