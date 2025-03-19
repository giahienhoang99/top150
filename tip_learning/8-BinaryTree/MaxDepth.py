def maxDepth(self, root: Optional[TreeNode]) -> int:
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0
