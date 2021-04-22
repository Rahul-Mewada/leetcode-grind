"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        
Approach 1: Standard BFS

1) Start a BFS 
2) Keep track of levels
3) While on a level connect each sibling to the one on its right 
4) Rightmost elements connect to null
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        q = []
        
        q.append((root, 0))
        prev_node, prev_level = None, 0
        
        while q:
            curr_node, curr_level = q.pop(0)
            
            if curr_node.left:
                q.append((curr_node.left, curr_level+1))
            if curr_node.right:
                q.append((curr_node.right, curr_level+1))
            
            if prev_node and prev_level == curr_level:
                prev_node.next = curr_node
                
            curr_node.next = None
            prev_node, prev_level = curr_node, curr_level
                
        return root