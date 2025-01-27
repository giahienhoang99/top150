public class AddTwoNumbers {
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

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode pointer = new ListNode(-1);
        ListNode cur = pointer;

        while (l1 != null || l2 != null) {
            if (l1 == null) {
                while (l2 != null) {
                    cur.next = new ListNode((l2.val + carry) % 10);
                    carry = (l2.val + carry) / 10;
                    cur = cur.next;
                    l2 = l2.next;
                }
                break;
            }
            if (l2 == null) {
                while (l1 != null) {
                    cur.next = new ListNode((l1.val + carry) % 10);
                    carry = (l1.val + carry) / 10;
                    cur = cur.next;
                    l1 = l1.next;
                }
                break;
            }
            cur.next = new ListNode((l1.val + l2.val + carry) % 10);
            carry = (l1.val + l2.val + carry) / 10;
            cur = cur.next;
            l1 = l1.next;
            l2 = l2.next;
        }

        if (carry != 0) {
            cur.next = new ListNode(1);
        }
        
        return pointer.next;
    }

    // more concise solution
    public ListNode addTwoNumbersConcise(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(0);
        ListNode current = dummyHead;
        int carry = 0;

        // Traverse both linked lists
        while (l1 != null || l2 != null) {
            int x = (l1 != null) ? l1.val : 0;
            int y = (l2 != null) ? l2.val : 0;
            int sum = x + y + carry;
            carry = sum / 10;
            current.next = new ListNode(sum % 10);
            current = current.next;

            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }

        // Handle remaining carry
        if (carry != 0) {
            current.next = new ListNode(carry);
        }

        return dummyHead.next;
    }
}
