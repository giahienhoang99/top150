package 8_LinkedList;

public class ReverseLinkedList {
    class ListNode {
        int val;
        ListNode next;
    
        ListNode() {
        }
    
        ListNode(int val) {
            this.val = val;
        }
    
        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }
    public ListNode reverseListIterative(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode prev = null;
        ListNode cur = head;
        ListNode next;
        
        while (cur != null) {
            next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }

        return prev;
    }
    
}
