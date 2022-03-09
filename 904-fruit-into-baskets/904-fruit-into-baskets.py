"""
-Subarray can have only 2 different types of fruits
- we want to return the length of the maximum subarray with no greater than 2 types of fruits

 1 2 3 1 2 2
       s   f

cur_freq = { 
    1 : 1,
    2 : 2
}
max = 3
"""

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        slow = 0
        cur_freq = {}
        max_len = 0
        
        for fast in range(len(fruits)):
            if fruits[fast] in cur_freq:
                cur_freq[fruits[fast]] += 1
            else:
                cur_freq[fruits[fast]] = 1
            
            while len(cur_freq) > 2:
                if cur_freq[fruits[slow]] == 1:
                    cur_freq.pop(fruits[slow])
                else:
                    cur_freq[fruits[slow]] -= 1
                slow += 1
            
            max_len = max(max_len, fast - slow + 1)
        
        return max_len