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
    public ListNode reverseList(ListNode head) {
        ListNode cur = head;
        ListNode temp;
        
        if(head == null) {
            return head;
        }
        

        while(cur.next != null) {
            temp = cur.next;            
            cur.next = cur.next.next;
            temp.next = head;
            head = temp;
        }
        
        return head;
        
    }
}