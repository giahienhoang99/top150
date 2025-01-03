package learning;

import java.util.LinkedList;
import java.util.Queue;

public class IsCousins {
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

    // level order traversal (bfs) with early stopping (found 1 node but not the
    // other)
    public boolean isCousins1(TreeNode root, int x, int y) {
        // cousins = nodes w/ same level and different parents
        // level order traversal using a queue
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.add(root);
        boolean seenX = false;
        boolean seenY = false;
        while (!q.isEmpty()) {
            int qSize = q.size();
            
            // check current level nodes only
            while (qSize > 0) {
                TreeNode cur = q.poll();
                // check if seen x and y
                if (cur.val == x) {
                    seenX = true;
                }
                if (cur.val == y) {
                    seenY = true;
                }
                // enqueue children if exists
                if (cur.left != null) {
                    q.add(cur.left);
                }
                if (cur.right != null) {
                    q.add(cur.right);
                }
                // check if same parent
                if (cur.left != null && cur.right != null) {
                    if ((cur.left.val == x || cur.left.val == y) && (cur.right.val == x || cur.right.val == y)) {
                            return false;
                        }
                    }
                }
                qSize--;
            }

            if (seenX && seenY) {
                return true;
            }
            if (seenX || seenY) {
                return false;
            }
        }
        return false;
    }

    // recursive dfs solution
    private int lx = 0;
    private int ly = 0;
    private TreeNode px;
    private TreeNode py;

    public boolean isCousins2(TreeNode root, int x, int y) {
        // check if same level and different parent
        getLevelsAndParents(root, x, y, 0, null);
        return lx == ly && px != py;
    }
    // recursive helper function
    // calculates the levels of x and y and get their parents
    private void getLevelsAndParents(TreeNode root, int x, int y, int depth, TreeNode parent) {
        if (root == null) {
            return;
        }
        if (root.val == x) {
            lx = depth;
            px = parent;
        }
        if (root.val == y) {
            ly = depth;
            py = parent;
        }
        getLevelsAndParents(root.left, x, y, depth + 1, root);
        getLevelsAndParents(root.right, x, y, depth + 1, root);
    }
}
