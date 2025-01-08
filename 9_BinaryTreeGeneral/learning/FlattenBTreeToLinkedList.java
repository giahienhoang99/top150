package learning;

import java.util.Stack;

public class FlattenBTreeToLinkedList {
    public void flatten(TreeNode root) {
        if (root == null) {
            return;
        }

        TreeNode prev = null;

        Stack<TreeNode> s = new Stack();
        s.push(root);

        while (!s.isEmpty()) {
            TreeNode cur = s.pop();
            
            // in place
            if (prev != null) {
                prev.right = cur;
                prev.left = null;
            }

            // have to push right->left so order when pop() is left->right
            if (cur.right != null) {
                s.push(cur.right);
            }
            if (cur.left != null) {
                s.push(cur.left);
            }

            prev = cur;
        }
    }
}
