public class RemoveNthNodeFromEnd {
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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null || head.next == null)
            return null;
        ListNode cur = head;
        int length = 0;

        while (cur != null) {
            length++;
            cur = cur.next;
        }

        length -= n;
        if (length == 0)
            return head.next;
        int track = 0;
        cur = head;

        while (cur != null) {
            track++;
            if (track == length) {
                cur.next = (cur.next == null) ? null : cur.next.next;
                break;
            }
            cur = cur.next;
        }

        return head;
    }
}
