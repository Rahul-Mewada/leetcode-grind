'''
1 1 0 0 0 
1 1 0 0 0 
0 0 1 0 0 
0 0 0 1 1
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        print(len(grid), len(grid[0]))
        islands = Islands(grid)
        return islands.count_islands()
    
class Islands:
    def __init__(self, grid):
        self.grid = grid
        
    
    def count_islands(self):
        num_islands = 0
        queue = deque()
        count = 0
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == "1":
                    self.grid[row][col] = '0'
                    self.bfs(queue, row, col)
                    count += 1
                    
        return count
        
        
    def bfs(self, queue, row, col):
        queue.append((row,col))
        while queue:
            cur_row, cur_col = queue.popleft()
            self.grid[cur_row][cur_col] = '0'
            neighbors = self.get_neighbors(cur_row, cur_col)
            for neighbor in neighbors:
                queue.append(neighbor)
        
            
    def get_neighbors(self, row, col):
        directions = [
            (1,0), # right
            (0,1), # up
            (-1,0), # left
            (0,-1) # down
        ]
        results = []
        for d_row, d_col in directions:
            new_row, new_col = row + d_row, col + d_col
            if 0 <= new_row < len(self.grid) and 0 <= new_col < len(self.grid[0]) and self.grid[new_row][new_col] == '1':
                self.grid[new_row][new_col] = '0'
                results.append((new_row, new_col))
        return results