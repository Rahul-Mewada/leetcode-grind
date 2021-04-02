'''
Brute force- try all possible combinations O(n!)
Greedy approach?

BFS O(N) with memoization
1) Neighbors = indices you can jump to from your current position
2) Prioritize highest neighbors first
3) Keep track of levels
4) When you reach the end, return the number of levels

q - [(1,1), (3,1)]
visited = {0, }
[2,3,1,1,4]
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        min_jumps = self.bfs(nums)
        if min_jumps:
            return min_jumps
        else:
            print("Cannot reach end")
            return None
        
    def bfs(self, nums):
        queue = [] # FIFO stack using a list
        queue.append((0, 0)) # (index, level)
        visited = set()
        
        while len(queue) != 0:
            index, level = queue.pop(0) # pops from the start and appends from the end
            if index == len(nums)-1:
                return level
            
            if index not in visited:
                max_jumps = nums[index]
                while max_jumps > 0:
                    if max_jumps + index < len(nums):
                        queue.append((max_jumps + index, level+1))
                    max_jumps -= 1
                    
            visited.add(index)
        return None