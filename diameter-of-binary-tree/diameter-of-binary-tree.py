# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Return the longest path between any two nodes 

1) 
'''


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        global max_length 
        max_length = 0
        
        if not root.left and not root.right:
            return 0
        
        self.dfs(root)
        
        return max_length
        
    def dfs(self, current):
        global max_length
        if not current.left and not current.right:
            return 1
        
        left, right = 0,0
        
        if current.left:
            left = self.dfs(current.left)
        if current.right:
            right = self.dfs(current.right)
            
        max_length = max(max_length, left+right)
        
        return max(left, right)+1