'''
cur_direct 
- north = [0, 1]
- south = [0, -1]
- east = [1, 0]
- west = [-1, 0]

                n      e        s       w
multipliers = [[0,1], [1,0], [0, -1], [-1, 0]]
'''

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        multipliers = [[0,1], [1,0], [0, -1], [-1, 0]]
        cur_dir = 0
        cur_pos = [0,0]
        
        for instruction in instructions:
            if instruction == 'G':
                cur_pos[0] += multipliers[cur_dir][0]
                cur_pos[1] += multipliers[cur_dir][1]
            else:
                cur_dir = self.changeDirection(cur_dir, instruction)
            
        if (cur_pos[0] == 0 and cur_pos[1] == 0) or cur_dir != 0:
            return True
        else:
            return False
            
    def changeDirection(self, index, direction):
        if direction == 'L':
            index -= 1
        else:
            index += 1
            
        if index < 0:
            return 3
        elif index > 3:
            return 0
        else:
            return index
        