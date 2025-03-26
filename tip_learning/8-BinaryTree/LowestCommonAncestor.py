from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ O(n^2)
        def is_ancestor(node, child) -> bool:
            if not node:
                return False
            if node == child:
                return True
            left = is_ancestor(node.left, child)
            right = is_ancestor(node.right, child)
            if left or right:
                return True
            
        def is_ancestor_both(node, p, q) -> bool:
            return is_ancestor(node, p) and is_ancestor(node, q)

        lca = None
        
        def dfs(node):
            nonlocal lca
            if not node:
                return
            if is_ancestor_both(node, p, q):
                lca = node
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return lca
        """
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right