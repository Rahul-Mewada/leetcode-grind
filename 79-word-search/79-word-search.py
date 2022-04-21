'''
 A B C E    A B C E S E E E F S 
 S F E S          i
 A D E E

Visited - A,B,C
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    exists = self.dfs(board, row, col, word, 0, set((row, col)))
                    if exists:
                        return True
        return False
    
    def dfs(self, board, cur_row, cur_col, word, i, visited):
        if i == len(word) - 1:
            return board[cur_row][cur_col] == word[i]
        
        if board[cur_row][cur_col] != word[i]:
            return False
        
        visited.add((cur_row, cur_col))
        
        for new_row, new_col in self.valid_neighbors(board, cur_row, cur_col, visited):
            exists = self.dfs(board, new_row, new_col, word, i+1, visited)
            if exists:
                return True
            if (new_row, new_col) in visited:
                visited.remove((new_row, new_col))
        
        return False
        
        
    
    
    def valid_neighbors(self, board, row, col, visited):
        directions = [
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        ]
        results = []
        for d_row, d_col in directions:
            new_row, new_col = row + d_row, col + d_col
            if 0 <= new_row < len(board) and 0 <= new_col < len(board[row]) and (new_row, new_col) not in visited:
                results.append((new_row, new_col))
        return results