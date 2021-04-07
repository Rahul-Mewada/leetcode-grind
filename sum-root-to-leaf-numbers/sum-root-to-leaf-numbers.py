# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.dfs(root, '')
        
    def dfs(self, node, path_string):
        if not node.left and not node.right:
            return int(path_string+str(node.val))
        
        total= 0
        if node.left:
            total += self.dfs(node.left, path_string+str(node.val))
        if node.right: 
            total += self.dfs(node.right, path_string+str(node.val))
        
        return total