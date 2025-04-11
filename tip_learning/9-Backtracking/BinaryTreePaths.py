from typing import List, Optional


def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    paths = []
    path = [str(root.val)]
        
    def backtrack(node):
        if not (node.left or node.right):
            paths.append("->".join(path))
            return

        if node.left:
            path.append(str(node.left.val))
            backtrack(node.left)
            path.pop()
        
        if node.right:
            path.append(str(node.right.val))
            backtrack(node.right)
            path.pop()
    
    backtrack(root)
    return paths
