# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
 1 2 3 4 5 None
 h c
 
 2 1 3 4 5 None
 h p c
 
 3 2 1 4 5 None
 h   p c
 4 3 2 1 5 None
 
 5 4 3 2 1 None
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        cur = head.next
        prev = head
        while cur:
            prev.next = cur.next
            cur.next = head
            head = cur
            cur = prev.next
            
        return head