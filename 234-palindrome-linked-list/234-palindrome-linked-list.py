# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
 1 2 2 1
sf
   s f
     s   f

 1 2 
 h
 1 2
 h
    
'''
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        if not head.next.next:
            return head.val == head.next.val
        
        second_head, tail = self.returnMid(head)
        tail.next = None
        first_head = head
        second_head = self.reverse(second_head)

        while second_head:
            if first_head.val != second_head.val:
                return False
            second_head = second_head.next
            first_head = first_head.next
        
        return True 
        
    def returnMid(self, head):
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        return (slow.next, slow) if fast else (slow, prev)
            
            
    def reverse(self, head):
        cur = head.next
        prev = head
        while cur:
            temp = cur
            prev.next = cur.next
            temp.next = head
            head = temp
            cur = prev.next
        return head
            
            
            
            