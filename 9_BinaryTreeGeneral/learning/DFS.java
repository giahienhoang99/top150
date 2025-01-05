package learning;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class DFS {
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
    
    // Iterative preorder, inorder, postorder traversal    
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) return res;
        Stack<TreeNode> s = new Stack<>();
        s.push(root);
        while (!s.isEmpty()) {
            TreeNode cur = s.pop();
            res.add(cur.val);
            // Push right child first, so left child is processed first
            if (cur.right != null) {
                s.push(cur.right);
            }
            if (cur.left != null) {
                s.push(cur.left);
            }
        }
        return res;
    }
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> s = new Stack<>();
        TreeNode cur = root;
        while (cur != null || !s.isEmpty()) {
            // traverse left subtree
            while (cur != null) {
                s.push(cur);
                cur = cur.left; // update cur
            }
            // process node (add to res)
            cur = s.pop();
            res.add(cur.val);
            // traverse right subtree
            cur = cur.right;
        }
        return res;
    }
    
}
