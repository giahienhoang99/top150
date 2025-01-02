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

    // my solution using level order traversal or bfs on tree
    public boolean isCousins(TreeNode root, int x, int y) {
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
                if (cur.left != null & cur.right != null) {
                    if (cur.left.val == x || cur.left.val == y) {
                        if (cur.right.val == x || cur.right.val == y) {
                            // dont have to check which node is which since every node is unique
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
}
