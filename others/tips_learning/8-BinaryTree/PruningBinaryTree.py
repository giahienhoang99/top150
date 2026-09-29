from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        dfs again
        a node is pruned when these conditions are met:
            - its val is 0
            - its subtrees dont have a 1
        => dfs function to recursively return a bool and also prune tree as we go
        => tree nodes with 1 return a True that bubbles up
        => use the bool to decide to prune a node or not
        """
        def dfs(node) -> bool:
            if not node:
                return False
            
            left_has_1 = dfs(node.left)
            right_has_1 = dfs(node.right)
            
            if not left_has_1 and not right_has_1 and node.val == 0:
                return False
            
            if not left_has_1:
                # prune left
                node.left = None
            if not right_has_1:
                # prune right
                node.right = None

            return node.val == 1 or left_has_1 or right_has_1
        
        return root if dfs(root) else None