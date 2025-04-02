def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    paths = []

    def backtrack(node, path):
        if not node:
            return

        if not (node.left or node.right):
            paths.append(path)
            return

        if node.left:
            temp1 = path
            path += "->" + str(node.left.val)
            backtrack(node.left, path)
            path = temp1

        if node.right:
            temp2 = path
            path += "->" + str(node.right.val)
            backtrack(node.right, path)
            path = temp2

    backtrack(root, str(root.val))
    return paths
