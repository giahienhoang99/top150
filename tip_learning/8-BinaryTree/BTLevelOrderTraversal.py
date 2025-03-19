import collections


def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    result = []
    q = collections.deque()
    q.append(root)
    while q:
        level = []
        for _ in range(len(q)):
            cur = q.popleft()
            level.append(cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        result.append(level)
    return result
