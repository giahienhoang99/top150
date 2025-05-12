import math
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(self, root: Optional[TreeNode]) -> bool:

    # dfs to check if valid
    def dfs(node, floor, ceil) -> bool:
        if not node:
            return True
        if not floor < node.val < ceil:
            return False
        return dfs(node.left, floor, node.val) and dfs(node.right, node.val, ceil)

    return dfs(root, -math.inf, math.inf)
