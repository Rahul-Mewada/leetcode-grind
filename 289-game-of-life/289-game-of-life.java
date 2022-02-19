/*
init
 0  1  0
 0  0  1
 1  1  1
 0  0  0
  
result
 0 -1  0
 2  0  1
 1  1  1
 0  0  0
 
 let use these designations
 -1 live -> dead
  2 dead -> live
  
  
  for()
    for()
        playOnce(); -> (numLives)
        cleanMatix();

O(MN) time
O(1) space not counting the original 

*/


class Solution {
    public void gameOfLife(int[][] board) {
        printState(board);
        playOnce(board);
        
        printState(board);
        cleanMatrix(board);

        printState(board);
        return;
    }
    
    public void playOnce(int[][] board) {
        // implements the rules of the game
        // designations: -1 (live -> dead), 2 (dead -> live)
        int numNeighbors;
        for(int row = 0; row < board.length; row++) {
            for(int col = 0; col < board[row].length; col++) {
                numNeighbors = numLiveNeighbors(board, row, col);
                if(isLive(board, row, col) && (numNeighbors < 2 || numNeighbors > 3)) {
                    // designate for death
                    board[row][col] = -1;
                } else if(!isLive(board, row, col) && numNeighbors == 3) {
                    // designate for death
                    board[row][col] = 2;
                }
            }
        }
    }
    
    
    public int numLiveNeighbors(int[][] board, int row, int col) {
        // returns the num of neighbours for a particular co-ordinate
        int[][] neighbors = {
            {row + 1, col},
            {row - 1, col},
            {row, col + 1},
            {row, col - 1},
            {row + 1, col + 1},
            {row - 1, col + 1},
            {row + 1, col - 1},
            {row - 1, col - 1}
        };
        
        int numLive = 0;
        int neighborRow;
        int neighborCol;
        for(int[] neighbor : neighbors) {
            neighborRow = neighbor[0];
            neighborCol = neighbor[1];
            
            if(inBounds(board, neighborRow, neighborCol)){
                if(isLive(board, neighborRow, neighborCol)) numLive++;
            }
        }
        return numLive;
    }
    
    public void cleanMatrix(int[][] board) {
        // applies the live/death designations on pieces marked as such
        for(int row = 0; row < board.length; row++) {
            for(int col = 0; col < board[row].length; col++) {
                if(board[row][col] == -1) {
                    board[row][col] = 0;
                } else if(board[row][col] == 2) {
                    board[row][col] = 1;
                }
            }
        }
    }
    
    public boolean inBounds(int[][] board, int row, int col) {
        // returns true if a co-ordinate exists within the bounds of the board
        if((row >= 0 && row < board.length) && (col >= 0 && col < board[0].length)) return true;
        return false;
    }
    
    public boolean isLive(int[][] board, int row, int col) {
        // returns true if the position is a live cell at that iteration
        if(board[row][col] == 1 || board[row][col] == -1) return true;
        return false;
    }
    
    public void printState(int[][] board) {
        System.out.println();
        for(int row = 0; row < board.length; row++) {
            for(int col = 0; col < board[row].length; col++) {
                System.out.print(board[row][col] + ", ");
            }
            System.out.println();
        }
        System.out.println();
        return;
    }
}