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
    public ListNode deleteDuplicates(ListNode head) {
        ListNode slow = head;
        if(slow == null) {
            return head;
        }
        ListNode fast = slow.next;

        deleteDups(slow, fast);
        return head;
        
    }
    
    
    // 1 -> 2 -> 3 -> 3 -> null
    //           s          f
    
    public void deleteDups(ListNode slow, ListNode fast) {
        if(fast == null) {
            slow.next = null;
            return;
        }
        
        if(slow.val != fast.val) {
            slow.next = fast;
            deleteDups(slow.next, fast.next);
        } else {
            deleteDups(slow, fast.next);
        }
    }
}