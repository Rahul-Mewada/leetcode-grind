# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Simple DFS question
- Return all root to leaf paths where each path's sum equals target

DFS + path array + running total

1) Start at root node
2) update path and sum
3) dfs on left and right
4) on reaching a leaf node: check for sums and update paths
'''

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        results = []
        self.dfs(root, [], 0, results, targetSum)
        if root == []:
            return 1
        return results
    
    def dfs(self, node, path, cur_sum, results, target):
        if node:
            if not node.left and not node.right:
                cur_sum += node.val
                if cur_sum == target:
                    results.append(path+[node.val])
                return


            if node.left:
                self.dfs(node.left, path+[node.val], cur_sum+node.val, results, target)
            if node.right:
                self.dfs(node.right, path+[node.val], cur_sum+node.val, results, target)
        
        return 
        
                