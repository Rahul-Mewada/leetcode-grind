# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Simple DFS

1) calculate the path sum during DFS and if it matches the target -> Return true

'''


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root == None:
            return False
        path_sum = 0
        return self.dfs(root, targetSum, path_sum)
        
    def dfs(self, node, target, path_sum):
        if not node.left and not node.right:
            path_sum += node.val
            return path_sum == target
        
        path_sum += node.val
        
        meets_right_target, meets_left_target = False, False
        
        if node.left:
            meets_left_target = self.dfs(node.left, target, path_sum)
        if node.right:
            meets_right_target = self.dfs(node.right, target, path_sum)
        
        return meets_left_target or meets_right_target 
        