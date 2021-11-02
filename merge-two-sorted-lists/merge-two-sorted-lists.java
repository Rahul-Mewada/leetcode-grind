/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        
        ListNode l3 = new ListNode();
        ListNode current = l3;
        
        if(l1 == null && l2 == null) {
            return null;
        }
        
        while(l1 != null && l2 != null) {
            
            int low;
            if(l1.val >= l2.val) {
                low = l2.val;
                l2 = l2.next;
            } else {
                low = l1.val;
                l1 = l1.next;
            }
            
            //System.out.println(low);
            
            current.val = low;
            current.next = new ListNode();
            current = current.next;

        }

        if(l1 != null) {
            current.val = l1.val;
            current.next = l1.next;
        } else if(l2 != null) {
            current.val = l2.val;
            current.next = l2.next;
        }
        
        return l3;
    }
}