# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
1) Start at the root and update cur_sum, prev_sum and max_sum
2) Recursive call to the left and right
3) Update 
'''
class Solution:
    
    def maxPathSum(self, root: TreeNode) -> int:
        global max_sum
        cur_sum = root.val
        max_sum = cur_sum
        
        self.findMax(root)
        return max_sum
    
    def findMax(self, node):
        global max_sum
        if not node.left and not node.right:
            max_sum = max(max_sum, node.val)
            return node.val
        
        enclosed_sum = node.val
        left_max, right_max = 0,0
        if node.left:
            left_max = self.findMax(node.left)
            enclosed_sum += left_max
        if node.right:
            right_max = self.findMax(node.right)
            enclosed_sum += right_max
            
        
        optimum_path_sum = node.val + max(left_max, right_max, 0)
        
        max_sum = max(max_sum, optimum_path_sum, enclosed_sum, node.val)
        
        return optimum_path_sum
        
        
        