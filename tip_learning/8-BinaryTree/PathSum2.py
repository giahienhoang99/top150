from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, cur_list, cur_sum):
            if not node:
                return
            
            cur_list.append(node.val)
            cur_sum += node.val

            if not node.left and not node.right:
                if cur_sum == targetSum:
                    result.append(list(cur_list))

            dfs(node.left, cur_list, cur_sum)
            dfs(node.right, cur_list, cur_sum)

            cur_list.pop()
            
        dfs(root, [], 0)
        return result