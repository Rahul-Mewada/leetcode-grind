/*
DFS -> return smallest value (score) in the path when you reach the destination

we want a path leading from (0,0) to (m-1, n-1) that has the maximum score 

 5 4 5
 1 2 6
 7 4 6
 
min - 4
cur - 6
pr = [2 1]
*/

class Solution {
    public int maximumMinimumPath(int[][] grid) {
        
        Queue<int[]> maxHeap = new PriorityQueue<int[]>((a, b) -> Integer.compare(grid[b[0]][b[1]], grid[a[0]][a[1]]));
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        
        visited[0][0] = true;
        maxHeap.offer(new int[] {0, 0});
        
        int min = Integer.MAX_VALUE;
        
        int[][] directions = new int[][] {
            {1,0},
            {-1,0},
            {0, -1},
            {0, 1}
        };
        
        // maximise using heap
        // minimize using Math.min()
        while(!maxHeap.isEmpty()) {
            int[] curPos = maxHeap.poll();
            int row = curPos[0];
            int col = curPos[1];
            
            visited[row][col] = true;
            min = Math.min(min, grid[row][col]);
            
            for(int[] direction : directions) {
                int x = row + direction[0];
                int y = col + direction[1];
                
                if(inBounds(grid, x, y) && !visited[x][y]) {
                    maxHeap.offer(new int[] {x, y});
                }
            }
            
            if(row == grid.length-1 && col == grid[0].length - 1) break;
            
        }
        
        return min;
    }
    
    
    
    public boolean inBounds(int[][] grid, int row, int col) {
        if(row >= 0 && row < grid.length && col >= 0 && col < grid[0].length) {
            return true;
        }
        
        return false;
    }
    
    
    
}