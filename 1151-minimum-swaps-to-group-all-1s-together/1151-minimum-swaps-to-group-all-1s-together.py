'''
 1 0 1 0 1 0 0 1 1 0 1
     l         r
           
           
total_ones = 6
cur_ones = 3
min_swaps = 3
  
'''
from math import inf
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        if len(data) == 1:
            return 0
        
        min_swaps = float(inf)
        total_ones, cur_ones, left, right = 0,0,0,0
        for num in data:
            if num == 1:
                total_ones += 1
        
        if total_ones <= 1:
            return 0
        
        while right < len(data):
            if data[right] == 1:
                cur_ones += 1
            
            while right < len(data) and (right - left + 1) == total_ones:
                min_swaps = min(min_swaps, total_ones - cur_ones)
                if data[left] == 1:
                    cur_ones -= 1
                left += 1
                
                right += 1
                if right < len(data) and data[right] == 1:
                    cur_ones += 1
            
            right += 1
            
        return min_swaps
            