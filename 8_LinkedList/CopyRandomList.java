import java.util.HashMap;

public class CopyRandomList {
    class Node {
        int val;
        Node next;
        Node random;
    
        public Node(int val) {
            this.val = val;
            this.next = null;
            this.random = null;
        }
    }

    public Node copyRandomList(Node head) {
        if (head == null)
            return null;

        // Step 1: Create a mapping from original nodes to their copies
        HashMap<Node, Node> map = new HashMap<>();
        Node cur = head;
        while (cur != null) {
            map.put(cur, new Node(cur.val));
            cur = cur.next;
        }

        // Step 2: Assign next and random pointers for the copied nodes
        cur = head;
        while (cur != null) {
            Node copy = map.get(cur);
            copy.next = map.get(cur.next); // Set the next pointer
            copy.random = map.get(cur.random); // Set the random pointer
            cur = cur.next;
        }

        // Step 3: Return the deep copy's head
        return map.get(head);
    }    
}
