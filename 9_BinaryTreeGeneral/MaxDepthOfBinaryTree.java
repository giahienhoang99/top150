import java.util.LinkedList;
import java.util.Queue;

public class MaxDepthOfBinaryTree {
    public int maxDepthRecursive(TreeNode root) {
        // recursive approach
        if (root == null) {
            return 0;
        }
        return Math.max(maxDepth(root.left) + 1, maxDepth(root.right) + 1);
    }
    
}
