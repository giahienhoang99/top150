from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        - longest path does not have to pass through the root
        - dfs and keep updating the longest path:
            + max(cur longest path, sum of the path passing thru the node (= sum of depths of 2 subtrees)
        """
        max_path = 0
        def maxDepth(node):
            nonlocal max_path
            if not node:
                return 0
            left = maxDepth(node.left)
            right = maxDepth(node.right)
            # update max_path
            max_path = max(max_path, left + right)
            # return max depth of the node
            return 1 + max(left, right)
        maxDepth(root)
        return max_path