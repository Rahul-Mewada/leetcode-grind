# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Approach 1) 
1) if k is greater than the number of nodes, reduce it by checking the total number of node and taking k = k%n
2) loop through the list until you have k elements remaining 
3) split the lists at the partition and then move the right list to the front 


'''
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0:
            return head
        if not head or not head.next:
            return head
        n = 1
        current = head
        # counting the number of nodes in the list 
        while(current.next):
            n+=1
            current = current.next
            tail = current
        
        # reducing k if its greater than n
        if k >= n:
            k = k%n
        
        if k ==0:
            return head
        
        current = head
        num_left = n-1
        
        # finding the partition node
        while(num_left > k):
            current = current.next 
            num_left -= 1
            
        list2 = current.next
        current.next = None
        tail.next = head
        head = list2
        
        return head