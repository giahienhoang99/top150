public class MergeKSortedLists {
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
    
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) {
            return null;
        }
        if (lists.length == 1) {
            return lists[0];
        }
 
 
        ListNode res = merge(lists[0], lists[1]);
 
 
        for (int i = 2; i < lists.length; i++) {
            res = merge(res, lists[i]);
        }
 
 
        return res;
    }
 
 
    private ListNode merge(ListNode l1, ListNode l2) {
        ListNode pointer = new ListNode(0);
        ListNode cur = pointer;
 
 
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                cur.next = l1;
                l1 = l1.next;
            } else {
                cur.next = l2;
                l2 = l2.next;
            }
            cur = cur.next;
        }
 
 
        if (l1 != null) {
            cur.next = l1;
        } else {
            cur.next = l2;
        }
 
 
        return pointer.next;
    }
 
}
