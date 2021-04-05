# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        results = []
        q = []
        q.append((root, 0))
        average = -1
        count = 0
        cum_sum = 0
        cur_depth = 0

        while q:
            node, depth = q.pop(0)
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))
            
            if depth == cur_depth:
                cum_sum += node.val
                count += 1
            else:
                results.append(cum_sum/count)
                cum_sum, count = node.val,1
                cur_depth = depth
                
        results.append(cum_sum/count)
        return results  
 