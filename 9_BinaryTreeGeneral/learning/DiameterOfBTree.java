package learning;

public class DiameterOfBTree {
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
    private int diameter;
    public int diameterOfBinaryTree(TreeNode root) {
        diameter = 0;
        longestPath(root);
        return diameter;
    }
    private int longestPath(TreeNode root) {
        if (root == null) return 0;
        int longestLeft = longestPath(root.left);
        int longestRight = longestPath(root.right);
        
        diameter = Math.max(longestLeft + longestRight, diameter);

        return Math.max(longestLeft, longestRight) + 1;
    }
}
