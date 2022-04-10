'''
  0   1. 2. 3  4. 5. 6. 7  8
 [73,73,74,75,71,69,72,76,73]
                    i
 4
 3
  
  0  1  2  3  4  5  6  7
 [2, 1, 1, 0, 0, 0, 0, 0]
 
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = deque()
        results = [0 for _ in temperatures]
        
        for i, cur_temp in enumerate(temperatures):
            while s and temperatures[s[0]] < cur_temp:
                popped_index = s.popleft()
                results[popped_index] = i - popped_index
                
            s.appendleft(i)
            
        return results