# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
                                                        1
                                            2                       3
                                    4            5           6              
                                    
total_sum = 21
cur_sum = 12

left_sum = 4
right_sum = 5

max_sum = max(5 * (12 + 4), 4 * (12 + 5))

so we want the max(right_sum * (cur_sum + left_sum), left_sum * (cur_sum + right_sum)
If the node is not the root, then the cur_sum = total_sum - (left_sum + right_sum)
'''
from math import inf
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total_sum = self.get_total_sum(root)
        _, max_product = self.get_max_product(root, total_sum)
        
        return max_product % ((10**9) + 7)
    
    def get_max_product(self, root, total_sum):
        if not root:
            return (0,float(-inf))
        
        left_sum, left_max = self.get_max_product(root.left, total_sum)
        right_sum, right_max = self.get_max_product(root.right, total_sum)
        
        cur_sum = total_sum - (left_sum + right_sum)
        
        cur_max = max(right_sum * (cur_sum + left_sum), left_sum * (cur_sum + right_sum))
        
        return (root.val + left_sum + right_sum, max(cur_max, max(left_max, right_max)))
    
    def get_total_sum(self, root):
        if not root:
            return 0
        
        left_sum = self.get_total_sum(root.left)
        right_sum = self.get_total_sum(root.right)
        
        return (root.val + left_sum + right_sum)
            