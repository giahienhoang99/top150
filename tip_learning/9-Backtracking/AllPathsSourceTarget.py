def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    n = len(graph)
    paths = []
    path = [0]

    def backtrack(node):
        # end condition
        if node == n - 1:
            paths.append(list(path))
            return

        for neighbor in graph[node]:
            path.append(neighbor)
            backtrack(neighbor)
            path.pop()

    backtrack(0)
    return paths
