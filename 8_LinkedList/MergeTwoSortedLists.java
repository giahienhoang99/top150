public class MergeTwoSortedLists {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null || list2 == null) {
            return (list1 == null) ? list2 : list1;
        }

        ListNode pointer = new ListNode(-1);
        ListNode cur = pointer;

        while (list1 != null || list2 != null) {
            if (list1 == null) {
                while (list2 != null) {
                    cur.next = list2;
                    list2 = list2.next;
                    cur = cur.next;
                }
                break;
            }
            if (list2 == null) {
                while (list1 != null) {
                    cur.next = list1;
                    list1 = list1.next;
                    cur = cur.next;
                }
                break;
            }

            if (list1.val < list2.val) {
                cur.next = list1;
                list1 = list1.next;
            } else {
                cur.next = list2;
                list2 = list2.next;
            }
            cur = cur.next;
        }

        return pointer.next;
    }    
}
