# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
0 1 2 3 4 5 
s   m     e

0 1 2       3 4 5
s m e       s   e

01   2      
'''
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        
        return self.divide_and_conq(lists, 0, len(lists) - 1)
    
    def divide_and_conq(self, lists, start, end):
        print(start, end)
        if end - start + 1 <= 2:
            if start == end:
                return lists[start]
            return self.merge_two_lists(lists[start], lists[end])
        
        mid = (end + start)//2
        merge_one = self.divide_and_conq(lists, start, mid)
        merge_two = self.divide_and_conq(lists, mid+1, end)
        
        return self.merge_two_lists(merge_one, merge_two)
        
    
    def merge_two_lists(self, list_one, list_two):
        if not list_two and list_one:
            return list_one
        elif not list_one and list_two:
            return list_two
        elif not list_one and not list_two:
            return None
        
        merged = ListNode(None)
        cur = merged
        
        while list_one and list_two:
            if list_one.val < list_two.val:
                cur.next = ListNode(list_one.val)
                list_one = list_one.next
                cur = cur.next
            else:
                cur.next = ListNode(list_two.val)
                list_two = list_two.next
                cur = cur.next
        
        while list_one:
            cur.next = ListNode(list_one.val);
            list_one = list_one.next
            cur = cur.next
        
        while list_two:
            cur.next = ListNode(list_two.val)
            list_two = list_two.next
            cur = cur.next
        
        merged = merged.next
        return merged