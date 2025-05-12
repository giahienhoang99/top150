from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(node):
            return 1 + max(depth(node.left), depth(node.right)) if node else 0

        if not root:
            return True
        if abs(depth(root.left) - depth(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
