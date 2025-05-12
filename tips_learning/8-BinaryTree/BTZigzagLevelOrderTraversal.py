import collections


def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    q1 = collections.deque([root])
    q2 = collections.deque()
    results = []
    level = 0
    while q1 or q2:
        level_nodes = []
        if level % 2 == 0:
            for _ in range(len(q1)):
                cur = q1.popleft()
                level_nodes.append(cur.val)
                if cur.left:
                    q2.append(cur.left)
                if cur.right:
                    q2.append(cur.right)
        else:
            for _ in range(len(q2)):
                cur = q2.pop()
                level_nodes.append(cur.val)
                if cur.right:
                    q1.appendleft(cur.right)
                if cur.left:
                    q1.appendleft(cur.left)
        results.append(level_nodes)
        level += 1
    return results


def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    q = collections.deque([root])
    results = []
    level = 0
    while q:
        level_nodes = []
        for _ in range(len(q)):
            cur = q.popleft()
            level_nodes.append(cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        if level % 2 == 0:
            results.append(level_nodes)
        else:
            # 1st way: create a copy list from reverse order of level_nodes
            # results.append(level_nodes[::-1])
            # 2nd way: reverse level_nodes in place
            level_nodes.reverse()
            results.append(level_nodes)
        level += 1
    return results
