package learning;

import java.util.LinkedList;
import java.util.Queue;

public class CountNodesInCompleteBTree {
    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
    
    public int countNodes1(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int count = 0;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            TreeNode cur = q.poll();
            count++;

            if (cur.left != null) {
                q.add(cur.left);
            }
            if (cur.right != null) {
                q.add(cur.right);
            }
        }

        return count;
    }

    public int countNodes2(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return 1 + countNodes2(root.left) + countNodes2(root.right);
    }
}
