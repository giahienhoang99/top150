from collections import defaultdict, deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
    """
    - create an adj graph of the binary tree (dict: node.val -> [neighbors' vals])
    - perform bfs lv order traversal from target val
    """
    if not root:
        return []

    graph = defaultdict(list)

    def build_graph(node):
        if node.left:
            graph[node.val].append(node.left.val)
            graph[node.left.val].append(node.val)
            build_graph(node.left)
        if node.right:
            graph[node.val].append(node.right.val)
            graph[node.right.val].append(node.val)
            build_graph(node.right)

    # if range k = 0 then return the target node's val
    if k == 0:
        return [target.val]

    build_graph(root)
    q = deque([target.val])
    visited = set([target.val])
    level = 1
    result = []
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            for n in graph[cur]:
                if n in visited:
                    continue
                if level == k:
                    result.append(n)
                q.append(n)
                visited.add(n)
        level += 1

    return result
