package learning;

import java.util.ArrayList;
import java.util.List;

public class BTLevelOrderTraversal {
    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) {
            this.val = val;
        }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
    private List<List<Integer>> levels = new ArrayList<List<Integer>>();
    
    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null) return levels;
        helper(root, 0);
        return levels;
    }

    private void helper(TreeNode root, int depth) {
        if (root == null) {
            return;
        }
        if (levels.size() - 1 < depth) {
            List<Integer> level = new ArrayList<Integer>();
            level.add(root.val);
            levels.add(level);
        } else {
            List<Integer> level = levels.get(depth);
            level.add(root.val);
        }
        helper(root.left, depth + 1);
        helper(root.right, depth + 1);
    }
}
