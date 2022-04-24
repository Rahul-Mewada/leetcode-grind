# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
                                
                                        
                                        1
                                2               3
                           4          5    n           7
                        8      9     n 10            12  n
                        
                        1 *  3 2 * 4 5 n 7 * n 12 10 n 9 8 *
                        t     f        t        f  
            
             2    5
             lvl, node   
            
 level_lis = [[1], [3,2], [4, 5, 7]]
     queue = [ (2,n), (2,7), (3,8), (3,9)]
 isrevered = False
  prev_lvl = 1        
 
BFS
- trick is to alternate between left to right or right to left insertions for each level
'''
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        is_reversed = False
        queue = deque()
        queue.append((0, root))
        level_list = deque()
        results = []
        prev_level = 0
        
        while queue:
            cur_level, cur_node = queue.popleft()
            if cur_level == prev_level:
                self.add_to_level(is_reversed, level_list, cur_node)
            else:
                results.append(level_list)
                level_list = deque()
                is_reversed = not is_reversed
                self.add_to_level(is_reversed, level_list, cur_node)
                
            prev_level = cur_level
            if cur_node.left:
                queue.append((cur_level + 1, cur_node.left))
            if cur_node.right:
                queue.append((cur_level + 1, cur_node.right))
        
        if level_list:
            results.append(level_list)
        return results
    
    def add_to_level(self, is_reversed, level_list, node):
        if not node:
            return
        
        if is_reversed:
            level_list.appendleft(node.val)
        else:
            level_list.append(node.val)
        