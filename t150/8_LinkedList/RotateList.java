public class RotateList {
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
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null)
            return head;
        ListNode cur = head;
        int length = 0;
        ListNode prev = null;
        while (cur != null) {
            length++;
            if (cur.next == null) {
                cur.next = head;
                break;
            }
            if (cur.next.next == null)
                prev = cur;
            cur = cur.next;
        }
        int i = 0;
        k = k % length;
        while (i < length - k + 1) {
            i++;
            prev = prev.next;
            cur = cur.next;
        }
        prev.next = null;

        return cur;
    }
}
