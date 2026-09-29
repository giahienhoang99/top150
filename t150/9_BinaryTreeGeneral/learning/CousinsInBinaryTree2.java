package learning;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class CousinsInBinaryTree2 {
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
    public TreeNode replaceValueInTree(TreeNode root) {
        if (root == null)
            return null;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        List<Integer> lvSums = new ArrayList<>();
        int level = 0;

        // 1st bfs pass: calculate sum of nodes on each level
        while (!q.isEmpty()) {
            int numNodesCurLevel = q.size();
            for (int i = 0; i < numNodesCurLevel; i++) {
                TreeNode cur = q.poll();

                if (lvSums.size() - 1 < level) {
                    lvSums.add(0);
                }
                lvSums.set(level, lvSums.get(level) + cur.val);

                if (cur.left != null) {
                    q.add(cur.left);
                }
                if (cur.right != null) {
                    q.add(cur.right);
                }
            }
            level++;
        }
        // 2nd bfs pass: update new val for each node = sum of level nodes - sum of siblings (including themselves)
        root.val = 0;
        q.add(root);
        level = 1;  // start 1 not 0 since 0 is root level
        while (!q.isEmpty()) {
            int numNodesCurLevel = q.size();
            for (int i = 0; i < numNodesCurLevel; i++) {
                TreeNode cur = q.poll();
                int siblingSum = (cur.left != null ? cur.left.val : 0) + (cur.right != null ? cur.right.val : 0);

                if (cur.left != null) {
                    cur.left.val = lvSums.get(level) - siblingSum;
                    q.add(cur.left);
                }
                if (cur.right != null) {
                    cur.right.val = lvSums.get(level) - siblingSum;
                    q.add(cur.right);
                }
            }
            level++;
        }
        return root;
    }
}
