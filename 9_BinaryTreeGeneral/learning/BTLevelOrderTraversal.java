package learning;

import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.LinkedList;

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
    public List<List<Integer>> levelOrderRecursive(TreeNode root) {
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

    public List<List<Integer>> levelOrderIterative(TreeNode root) {
        List<List<Integer>> levels = new ArrayList<List<Integer>>();
        if (root == null) return levels;
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.add(root);
        while (!q.isEmpty()) {
            int qSize = q.size();
            List<Integer> level = new ArrayList<Integer>();
            while (qSize > 0) {
                TreeNode cur = q.poll();
                level.add(cur.val);
                if (cur.left != null) {
                    q.add(cur.left);
                }
                if (cur.right != null) {
                    q.add(cur.right);
                }
                qSize--;
            }
            levels.add(level);
        }
        return levels;
    }
}
